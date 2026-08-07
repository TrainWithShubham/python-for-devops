from fastapi import APIRouter, HTTPException

from services.logs_service import analyze_logs

router = APIRouter(tags=["logs"])


@router.get("/logs", status_code=200)
def get_log_summary(file: str | None = None):
    """Analyze a log file and return level counts. Defaults to the bundled app.log."""
    try:
        return analyze_logs(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Log file not found: {file}")


@router.get("/logs/errors", status_code=200)
def get_log_errors(file: str | None = None):
    """Return only the ERROR count from the log file."""
    try:
        summary = analyze_logs(file)
        return {"log_file": summary["log_file"], "error_count": summary["counts"]["ERROR"]}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Log file not found: {file}")


@router.get("/logs/warnings", status_code=200)
def get_log_warnings(file: str | None = None):
    """Return only the WARNING count from the log file."""
    try:
        summary = analyze_logs(file)
        return {"log_file": summary["log_file"], "warning_count": summary["counts"]["WARNING"]}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Log file not found: {file}")
