import psutil
# Takes threshold values (CPU, disk, memory) from user input
# Also fetches system metrics using a Python library (example: psutil)
# Compares metrics against thresholds
# Prints the result to the terminal


def check_system_health():
    cpu_threshold = int(input("Enter the CPU Threshold (%): "))
    memory_threshold = int(input("Enter the Memory Threshold (%): "))
    disk_threshold = int(input("Enter the Disk Usage Threshold (%): "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_memory = psutil.virtual_memory().percent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    current_disk = psutil.disk_usage('/').percent

    print(f"Current CPU Usage: {current_cpu}%")
    print(f"Current Memory Usage: {current_memory}%")
    print(f"Current Disk Usage: {current_disk}%")

    if current_cpu > cpu_threshold:
        print("CPU Alert: Usage exceeds threshold!")
    else:
        print("CPU is within safe limits.")

    if current_memory > memory_threshold:
        print("Memory Alert: Usage exceeds threshold!")
    else:
        print("Memory is within safe limits.")

    if current_disk > disk_threshold:
        print("Disk Alert: Usage exceeds threshold!")
    else:
        print("Disk is within safe limits.")


check_system_health()
