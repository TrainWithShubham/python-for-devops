#pyscript A updated LogScript using a class-based[oop] approach
import json
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

    def analyze_logs(self):
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}  
        for line in self.lines:
            line = line.strip()
            for level in self.counts:
                if f" {level} " in line:
                    self.counts[level] += 1
                    break

    def display_summary(self, show_errors: int = 5):
        print("\n=== Log Summary ===")
        for level, count in self.counts.items():
            print(f"{level}: {count}")

        error_lines = [line for line in self.lines if " ERROR " in line]
        if error_lines:
            print(f"\nFirst {min(show_errors, len(error_lines))} ERROR messages:")
            for line in error_lines[:show_errors]:
                print(f"- {line.strip()}")
        print("==================\n")

    def save_summary_txt(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"log_summary_{timestamp}.txt"
        try:
            with open(file_name, "w") as f:
                f.write("=== Log Summary ===\n")
                for level, count in self.counts.items():
                    f.write(f"{level}: {count}\n")
                f.write("==================\n")
            print(f"[INFO] Summary saved to '{file_name}'")
        except Exception as e:
            print(f"[ERROR] Could not write TXT summary: {e}")

class LogAnalyzerApp:

    def run(self):
        while True:
            print("1. Analyze log file")
            print("2. Exit")
            choice = input("Select an option (1 or 2): ").strip()

            if choice == "1":
                file_path = input("Enter path to log file: ").strip()
                analyzer = LogAnalyzer(file_path)
                if not analyzer.read_file():
                    continue
                analyzer.analyze_logs()
                analyzer.display_summary()
                analyzer.save_summary_txt()

            elif choice == "2":
                print("Exiting program.")
                break
            else:
                print("[ERROR] Invalid choice. Please select 1 or 2.\n")


if __name__ == "__main__":
    app = LogAnalyzerApp()
    app.run()
