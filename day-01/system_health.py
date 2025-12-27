import psutil

# Take threshold values from user input
def check_cpu(cpu_threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU Usage:", cpu_usage, "%")

    if cpu_usage > cpu_threshold:
        print("CPU ALERT")
    else:
        print("CPU OK")


def check_memory(mem_threshold):
    memory_usage = psutil.virtual_memory().percent
    print("Memory Usage:", memory_usage, "%")

    if memory_usage > mem_threshold:
        print("MEMORY ALERT")
    else:
        print("MEMORY OK")


def check_disk(disk_threshold):
    disk_usage = psutil.disk_usage('/').percent
    print("Disk Usage:", disk_usage, "%")

    if disk_usage > disk_threshold:
        print("DISK ALERT")
    else:
        print("DISK OK")


# User Input
cpu_threshold = int(input("Enter CPU threshold (%): "))
mem_threshold = int(input("Enter Memory threshold (%): "))
disk_threshold = int(input("Enter Disk threshold (%): "))

print("\n--- System Health Check ---")

# Function Calls
check_cpu(cpu_threshold)
check_memory(mem_threshold)
check_disk(disk_threshold)
