import psutil


def get_system_metrics(cpu_threshold: int | None = None):
    """Read CPU, memory and disk usage, and flag high CPU against a threshold."""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    if cpu_threshold is None:
        cpu_threshold = 85

    status = "High CPU" if cpu_percent > cpu_threshold else "Healthy"

    return {
        "cpu_percentage": cpu_percent,
        "memory_percentage": memory_percent,
        "disk_percentage": disk_percent,
        "cpu_threshold": cpu_threshold,
        "system_status": status
    }
        
