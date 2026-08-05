# Same log analyzer, now wrapped in a class so state and behavior live together.

import json
from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR", "UNKNOWN")


class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "UNKNOWN": 0,
        }

    def read_logs(self):
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found:", self.log_file)
            return []

    def analyze(self, lines):
        for line in lines:
            tokens = set(line.split())
            if "INFO" in tokens:
                self.counts["INFO"] += 1
            elif "WARNING" in tokens:
                self.counts["WARNING"] += 1
            elif "ERROR" in tokens:
                self.counts["ERROR"] += 1
            elif line.strip():
                self.counts["UNKNOWN"] += 1
        return self.counts

    def write_summary(self, path=None):
        if path is None:
            path = Path(self.log_file).with_suffix(".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.counts, f, indent=2)


def main():
    log_path = str(Path(__file__).parent / "app.log")
    analyzer = LogAnalyzer(log_path)

    lines = analyzer.read_logs()
    if not lines:
        print("No logs to analyze.")
        return

    result = analyzer.analyze(lines)
    analyzer.write_summary("custom_log_counts.json")

    print("Log Analysis Summary:")
    for level, count in result.items():
        print(f"  {level:7}: {count}")


if __name__ == "__main__":
    main()
