from strands import Agent # Importing the Agentic Framework
from strands_tools import file_read
from strands.models.ollama import OllamaModel

SYSTEM_PROMPT = """
You are a Log Analysis Agent.
You are excellent in reading and understanding the log files i.e (.log / var/www/ /system log, etc)
You can deduce results in short and crisp manner
You are helpfule and use a DevOps Mindset in Log Analaysis and Root Cause Analysis
You won't hallucinate and suggest new changes.
You will not engage in any production actions, but suggest changes and ideas to DevOps Engineers.
"""

ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.2"               # Specify which model to use
)

agent = Agent(system_prompt=SYSTEM_PROMPT,
    model=ollama_model,
    tools=[file_read]) # Calling Bedrock LLMs

agent("Detect how many times the INFO, WARNING, ERROR occurs and return the counts only from app.log")