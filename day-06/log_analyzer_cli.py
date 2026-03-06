#pyscript Python script into a CLI (Command Line Interface) tool using argparse
import argparse
from datetime import datetime
from typing import List, Dict

class LogAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lines: List[str] = []
        self.counts: Dict[str, int] = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def read_file(self) -> bool:
        try:
            with open(self.file_path, "r") as f:
                self.lines = f.readlines()
            return True
        except FileNotFoundError:
            print(f"[ERROR] File '{self.file_path}' not found.")
            return False
        except Exception as e:
            print(f"[ERROR] Could not read file: {e}")
            return False

    def analyze_logs(self, level_filter: str = None):
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for line in self.lines:
            line = line.strip()
            for level in self.counts:
                if f" {level} " in line:
                    if level_filter is None or level == level_filter:
                        self.counts[level] += 1
                    break

    def display_summary(self, level_filter: str = None, show_errors: int = 5):
        print("\n=== Log Summary ===")
        for level, count in self.counts.items():
            if level_filter is None or level == level_filter:
                print(f"{level}: {count}")

        error_lines = [line for line in self.lines if " ERROR " in line]
        if (level_filter is None or level_filter == "ERROR") and error_lines:
            print(f"\nFirst {min(show_errors, len(error_lines))} ERROR messages:")
            for line in error_lines[:show_errors]:
                print(f"- {line.strip()}")
        print("==================\n")

    def save_summary_txt(self, out_path: str, level_filter: str = None):
        try:
            with open(out_path, "w") as f:
                f.write("=== Log Summary ===\n")
                for level, count in self.counts.items():
                    if level_filter is None or level == level_filter:
                        f.write(f"{level}: {count}\n")
                f.write("==================\n")
            print(f"[INFO] Summary saved to '{out_path}'")
        except Exception as e:
            print(f"[ERROR] Could not write summary: {e}")

def main():
    parser = argparse.ArgumentParser(description="Analyze log files and generate summary")
    parser.add_argument('--file', required=True, help="Path to input log file")
    parser.add_argument('--out', required=True, help="Path to output summary file")
    parser.add_argument('--level', help="Optional log level filter (INFO, WARNING, ERROR)")

    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file)
    if not analyzer.read_file():
        return

    analyzer.analyze_logs(args.level)
    analyzer.display_summary(args.level)
    analyzer.save_summary_txt(args.out, args.level)

if __name__ == "__main__":
    main()
