import json

LOG_FILE = "app.log"

try:
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Log file not found: {LOG_FILE}")
    exit()

print("Total lines:", len(lines))

info_count = 0
warning_count = 0
error_count = 0

for line in lines:
    words = line.split()
    if "INFO" in words:
        info_count += 1
    if "WARNING" in words:
        warning_count += 1
    if "ERROR" in words:
        error_count += 1

print("INFO   :", info_count)
print("WARNING:", warning_count)
print("ERROR  :", error_count)

summary = {
    "INFO": info_count,
    "WARNING": warning_count,
    "ERROR": error_count,
}

with open("log_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("\nSaved summary to log_summary.json")