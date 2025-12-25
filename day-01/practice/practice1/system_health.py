import psutil

# Take threshold input from user
cpu_threshold = float(input("Enter CPU threshold (%): "))
memory_threshold = float(input("Enter Memory threshold (%): "))
disk_threshold = float(input("Enter Disk threshold (%): "))

# Get system usage
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

print("\n--- System Health Check ---")

# CPU check
if cpu_usage > cpu_threshold:
    print("CPU Usage HIGH:", cpu_usage, "%")
else:
    print("CPU Usage OK:", cpu_usage, "%")

# Memory check
if memory_usage > memory_threshold:
    print("Memory Usage HIGH:", memory_usage, "%")
else:
    print("Memory Usage OK:", memory_usage, "%")

# Disk check
if disk_usage > disk_threshold:
    print("Disk Usage HIGH:", disk_usage, "%")
else:
    print("Disk Usage OK:", disk_usage, "%")
