from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Simple DevOps API")

def analyze_logs(log_file_path: str):
    """
    Simple log analyzer:
    - Counts total lines
    - Counts 'ERROR' occurrences
    """
    summary = {"total_lines": 0, "errors": 0}
    try:
        with open(log_file_path, "r") as f:
            for line in f:
                summary["total_lines"] += 1
                if "ERROR" in line.upper():
                    summary["errors"] += 1
    except FileNotFoundError:
        summary["error"] = f"File '{log_file_path}' not found."
    return summary

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.get("/logs")
def logs_summary(log_file: str = "app.log"):
    """
    Log analyzer endpoint.
    Accepts optional 'log_file' query parameter.
    """
    return analyze_logs(log_file)