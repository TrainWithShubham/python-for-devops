# Log analysis agent - two ways to build it.
#   python run_agent.py           -> using langchain's create_agent
#   python run_agent.py custom    -> building the same loop by hand with langgraph
# Set OLLAMA_MODEL to switch models (default llama3.2).

import os
import sys
from pathlib import Path
from typing import Annotated, TypedDict

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from log_utils import LEVELS, count_log_levels, read_log_file, read_log_tail

APP_LOG = str(Path(__file__).parent / "app.log")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")

SYSTEM_PROMPT = (
    "You are a Log Analysis Agent for DevOps engineers. "
    "Always use the analyze_log_file tool to get exact counts, never guess. "
    "If the user asks for actual log text, use the read_log_tail tool. "
    "State the INFO/WARNING/ERROR counts, then give a one or two line summary. "
    "Suggest ideas only, never perform production actions."
)


@tool
def analyze_log_file(path: str) -> str:
    """Read a .log file and return the count of INFO, WARNING and ERROR lines."""
    counts = count_log_levels(read_log_file(path))
    return ", ".join(f"{level}={counts[level]}" for level in LEVELS)


@tool
def read_log_tail_tool(path: str, n: int = 5) -> str:
    """Return the last n lines of a log file."""
    return read_log_tail(path, n)


def make_model():
    return ChatOllama(model=MODEL, base_url="http://localhost:11434", temperature=0)


def build_agent():
    return create_agent(make_model(), tools=[analyze_log_file, read_log_tail_tool], system_prompt=SYSTEM_PROMPT)


# The same agent <-> tools loop that create_agent gives you, built by hand so you
# can see the moving parts: a message state, an agent node and a tools node.
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


def build_custom_agent():
    llm_with_tools = make_model().bind_tools([analyze_log_file, read_log_tail_tool])

    def call_model(state: AgentState):
        return {"messages": [llm_with_tools.invoke(state["messages"]) ]}

    graph = StateGraph(AgentState)
    graph.add_node("agent", call_model)
    graph.add_node("tools", ToolNode([analyze_log_file, read_log_tail_tool]))
    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", tools_condition)
    graph.add_edge("tools", "agent")
    return graph.compile()


def main():
    custom = len(sys.argv) > 1 and sys.argv[1] == "custom"

    print(f"Model: {MODEL}")
    print("Counts:", count_log_levels(read_log_file(APP_LOG)))

    agent = build_custom_agent() if custom else build_agent()

    messages = [HumanMessage(content=f"Analyze the log file at {APP_LOG}.")]
    if custom:
        messages.insert(0, SystemMessage(content=SYSTEM_PROMPT))

    result = agent.invoke({"messages": messages}, {"recursion_limit": 10})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
