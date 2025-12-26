class LogAnalyzer:
    def __init__(self, log_file, output_file): #
        self.log_file = log_file
        self.output_file = output_file
        self.log_counts = {
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0
        }

    def read_logs(self):
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()

                if not lines:
                    print("Log file is empty.")
                    return []

                return lines

        except FileNotFoundError:
            print("Log file not found.")
            return []

    def analyze_logs(self, lines):
        for line in lines:
            if "INFO" in line:
                self.log_counts["INFO"] += 1
            elif "WARNING" in line:
                self.log_counts["WARNING"] += 1
            elif "ERROR" in line:
                self.log_counts["ERROR"] += 1

    def write_summary(self):
        print("\n--- Log Summary ---")
        for level, count in self.log_counts.items():
            print(f"{level}: {count}")

        with open(self.output_file, "w") as file:
            file.write("--- Log Summary ---\n")
            for level, count in self.log_counts.items():
                file.write(f"{level}: {count}\n")

        print(f"\nSummary written to {self.output_file}")


def main():
    analyzer = LogAnalyzer("app.log", "log_summary.txt")
    log_lines = analyzer.read_logs()

    if not log_lines:
        return

    analyzer.analyze_logs(log_lines)
    analyzer.write_summary()


if __name__ == "__main__":
    main()
