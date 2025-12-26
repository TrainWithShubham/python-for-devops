def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        if not lines:
            print("[WARNING] Log file is empty")
            return []

        return lines

    except FileNotFoundError:
        print("[ERROR] Log file not found")
        return []


def analyze_logs(log_lines):
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in log_lines:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "WARNING" in line:
            log_counts["WARNING"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1

    return log_counts


def write_summary(summary, output_file):
    try:
        with open(output_file, "w") as file:
            for level, count in summary.items():
                file.write(f"{level}: {count}\n")
    except IOError as error:
        print(f"[ERROR] Failed to write summary file: {error}")


def main():
    log_file = "app.log"
    output_file = "log_summary.txt"

    log_lines = read_log_file(log_file)

    if not log_lines:
        print("[INFO] No logs to analyze")
        return

    summary = analyze_logs(log_lines)

    print("\nLog Summary:\n")
    for level, count in summary.items():
        print(f"{level}: {count}")

    write_summary(summary, output_file)
    print(f"\nSummary written to {output_file}")


if __name__ == "__main__":
    main()
