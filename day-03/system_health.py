#pyscipt to Check CPU Usages Updated with Listed Changes
import psutil
from typing import Optional


def get_threshold(prompt: str) -> Optional[int]:
    try:
        value = int(input(prompt))
        if not 0 <= value <= 100:
            raise ValueError("Threshold must be between 0 and 100.")
        return value
    except ValueError as error:
        print(f"[INPUT ERROR] {error}")
        return None


def check_resource_usage(resource_name: str, usage: float, limit: int) -> None:
    try:
        if usage > limit:
            print(
                f"[ALERT] {resource_name} usage HIGH: "
                f"{usage}% (limit: {limit}%)"
            )
        else:
            print(f"[OK] {resource_name} usage normal: {usage}%")
    except Exception as error:
        print(f"[ERROR] Unable to check {resource_name}: {error}")


def get_system_usage() -> dict:
    try:
        return {
            "CPU": psutil.cpu_percent(interval=1),
            "Memory": psutil.virtual_memory().percent,
            "Disk": psutil.disk_usage("/").percent,
        }
    except Exception as error:
        print(f"[SYSTEM ERROR] Failed to fetch system usage: {error}")
        return {}


def run_monitoring() -> None:
    cpu_limit = get_threshold("Enter CPU threshold : ")
    memory_limit = get_threshold("Enter Memory threshold : ")
    disk_limit = get_threshold("Enter Disk threshold : ")

    if None in (cpu_limit, memory_limit, disk_limit):
        print("Invalid input detected. Returning to menu.\n")
        return

    print("\nChecking system usage...\n")

    usage_data = get_system_usage()
    if not usage_data:
        print("No system data available. Returning to menu.\n")
        return

    check_resource_usage("CPU", usage_data["CPU"], cpu_limit)
    check_resource_usage("Memory", usage_data["Memory"], memory_limit)
    check_resource_usage("Disk", usage_data["Disk"], disk_limit)
    print()


def main() -> None:
    while True:
        print("1. Enter thresholds")
        print("2. Exit")

        choice = input("Select an option (1 or 2): ").strip()

        if choice == "1":
            run_monitoring()
        elif choice == "2":
            print("Exiting program")
            break
        else:
            print("[ERROR] Invalid choice. Please select 1 or 2.\n")


if __name__ == "__main__":
    main()
