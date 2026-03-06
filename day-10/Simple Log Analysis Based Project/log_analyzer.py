#pyscipt to analyze logs using python
import json
from datetime import datetime
from typing import Dict, List


def read_log_file(file_path: str) -> List[str]:
    try:
        with open(file_path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"[ERROR] File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"[ERROR] Could not read file: {e}")
        return []


def analyze_logs(lines: List[str]) -> Dict[str, int]:
    """Count INFO, WARNING, and ERROR messages."""
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        line = line.strip()
        for level in counts:
            if f" {level} " in line:
                counts[level] += 1
                break
    return counts


def save_summary_txt(counts: Dict[str, int], file_path: str) -> None:
    """Save log summary to a TXT file."""
    try:
        with open(file_path, "w") as f:
            f.write("=== Log Summary ===\n")
            for level, count in counts.items():
                f.write(f"{level}: {count}\n")
            f.write("==================\n")
        print(f"[INFO] Summary saved to '{file_path}'")
    except Exception as e:
        print(f"[ERROR] Could not write TXT summary: {e}")



def display_summary(counts: Dict[str, int], lines: List[str], show_errors: int = 5) -> None:
    print("\n=== Log Summary ===")
    for level, count in counts.items():
        print(f"{level}: {count}")
    error_lines = [line for line in lines if " ERROR " in line]
    if error_lines:
        print(f"\nFirst {min(show_errors, len(error_lines))} ERROR messages:")
        for line in error_lines[:show_errors]:
            print(f"- {line.strip()}")
    print("==================\n")


def main() -> None:
    while True:
        print("1. Analyze log file")
        print("2. Exit")
        choice = input("Select an option (1 or 2): ").strip()

        if choice == "1":
            file_path = input("Enter path to log file: ").strip()
            lines = read_log_file(file_path)
            if not lines:
                continue
            counts = analyze_logs(lines)
            display_summary(counts, lines)

            # Save output files with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            txt_file = f"log_summary_{timestamp}.txt"
            json_file = f"log_summary_{timestamp}.json"
            save_summary_txt(counts, txt_file)
            # save_summary_json(counts, json_file)

        elif choice == "2":
            print("Exiting log analysis program.")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1 or 2.\n")


if __name__ == "__main__":
    main()
