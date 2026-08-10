# AI Agents for DevOps (LangGraph + LangChain + Ollama)

Build a local, private AI agent that reads log files and explains what happened,
running entirely on your machine with [Ollama](https://ollama.com), orchestrated
with [LangGraph](https://langchain-ai.github.io/langgraph/) and
[LangChain](https://python.langchain.com/).

The idea that keeps it reliable: the tool does the math, the LLM writes the
story. A plain Python function counts the log levels (and is unit-tested without
any LLM); the agent just calls that tool and summarizes the result, so the
numbers are always right even if a small local model is imperfect at tool calls.

## What you'll learn

- What an agent is: an LLM that can decide to call tools
- Wrap a Python function as a LangChain `@tool`
- Run a local LLM with `ChatOllama` (no API keys, no cloud)
- Build an agent with `create_agent`, and see the same loop by hand with a
  LangGraph `StateGraph`

## Prerequisites

Ollama running with a model pulled:

```bash
ollama serve
ollama pull llama3.2                 # default (small, ~2GB)
curl http://localhost:11434/api/tags # should list llama3.2
```

`llama3.2` reliably calls the tool but its summaries can be generic. For sharper
output, pull a stronger model and set `OLLAMA_MODEL`:

```bash
ollama pull qwen3-coder:30b
OLLAMA_MODEL=qwen3-coder:30b python run_agent.py
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Files

- `app.log` — sample log
- `log_utils.py` — deterministic counting core (no LLM)
- `run_agent.py` — the agent (`create_agent`, plus a hand-built `StateGraph`)
- `test_log_utils.py` — tests for the counting core

```bash
python -m pytest .            # counting core, no Ollama needed
python run_agent.py           # the agent (needs Ollama)
python run_agent.py custom    # the hand-built StateGraph version
```

The demo prints the deterministic counts first, then the agent's summary, so you
always see correct numbers. `create_agent` (from `langchain.agents`) is the
LangChain 1.0 API; `run_agent.py custom` shows the same agent/tools loop built by
hand with `StateGraph`, `ToolNode` and a conditional edge.

## Practice

Wire up the agent yourself:

1. Create a `ChatOllama` model (`base_url="http://localhost:11434"`, `temperature=0`).
2. Pass the `analyze_log_file` tool to `create_agent(model, tools=[...], system_prompt=...)`.
3. Invoke it with a `HumanMessage` asking it to analyze `app.log`, and print the result.
4. Bonus: add a second tool (e.g. return the last N lines) and watch how it chooses.
5. The module now includes a `read_log_tail` tool so the agent can return the last N lines of the log file on request.
