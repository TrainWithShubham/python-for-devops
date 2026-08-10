import argparse
import json
import sys
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")

parser = argparse.ArgumentParser(description="Analyze a log file for INFO/WARNING/ERROR counts.")
parser.add_argument("--file", required=True, help="path to the log file")
parser.add_argument("--out", help="write the summary to this JSON file")
parser.add_argument("--level", choices=LEVELS, help="show the count for only this level")

args = parser.parse_args()

log_path = Path(args.file)
if not log_path.is_file():
    print(f"Error: log file not found: {args.file}", file=sys.stderr)
    sys.exit(2)

with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

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

counts = {
    "INFO": info_count,
    "WARNING": warning_count,
    "ERROR": error_count,
}

if args.level:
    print(f"{args.level}: {counts[args.level]}")
else:
    print("INFO   :", info_count)
    print("WARNING:", warning_count)
    print("ERROR  :", error_count)

if args.out:
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(counts, f, indent=2)
    print(f"Wrote summary to {args.out}")