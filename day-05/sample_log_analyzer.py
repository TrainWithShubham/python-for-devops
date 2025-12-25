# Day 05 - Log Analyzer (Sample File For your Reference)

class LogAnalyzer:
    def __init__(self, log_file):
        """
        __init__ function runs first and initializes
        the values into class variables.
        """
        self.log_file = log_file
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "UNKNOWN": 0}

    def read_logs(self):
        """
        Function to read logs from the given log file
        """
        try:
            with open(self.log_file, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found:", self.log_file)
            return []

    def analyze(self, lines):
        """
        Analyzer to count the error patterns & Counts
        """
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
            else:
                self.counts["UNKNOWN"] += 1

        return self.counts


def main():
    """
    Main Function as a single entrypoint to the program
    """
    analyzer = LogAnalyzer("app.log")
    lines = analyzer.read_logs()

    if not lines:
        print("No logs to analyze.")
        return

    result = analyzer.analyze(lines)

    print("Log Analysis Summary:")
    for level, count in result.items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    main()
