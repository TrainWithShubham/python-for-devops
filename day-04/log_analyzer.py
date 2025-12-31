def analyze_logs():
    log_file = "app.log"
    output_file = "log_summary.txt"

    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(log_file, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Log file is empty.")
                return

            for line in lines:
                if "INFO" in line:
                    log_count["INFO"] += 1
                elif "WARNING" in line:
                    log_count["WARNING"] += 1
                elif "ERROR" in line:
                    log_count["ERROR"] += 1
                else:
                    pass  # Ignore lines without known log levels

    except FileNotFoundError:
        print("Log file not found.")
        return

    # Print summary to terminal
    print(f"INFO: {log_count['INFO']}")
    print(f"WARNING: {log_count['WARNING']}")
    print(f"ERROR: {log_count['ERROR']}")

    # Write summary to output file
    with open(output_file, "w") as file:
        file.write("--- Log Summary ---\n")
        file.write(f"INFO: {log_count['INFO']}\n")
        file.write(f"WARNING: {log_count['WARNING']}\n")
        file.write(f"ERROR: {log_count['ERROR']}\n")

    print(f"\nSummary written to {output_file}")


if __name__ == "__main__":
    analyze_logs()