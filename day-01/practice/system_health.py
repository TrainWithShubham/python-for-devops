import psutil

def check_system_health():
    user_cpu_threshold = int(input("Enter the CPU Threshold (%): \n")) # take cpu threshold input from user
    user_memory_threshold = int(input("Enter the Memory Threshold (%): \n")) # take memory threshold input from user
    user_disk_threshold = int(input("Enter the Disk Usage Threshold (%): \n"))  # take disk usage threshold input from user
    
    current_cpu = psutil.cpu_percent(interval=1) # get current cpu usage
    current_memory = psutil.virtual_memory().percent # get current memory usage
    current_disk = psutil.disk_usage('/').percent # get current disk usage

    print(f"Current CPU Usage: {current_cpu}%") # print current cpu usage
    print(f"Current Memory Usage: {current_memory}%") # print current memory usage
    print(f"Current Disk Usage: {current_disk}%") # print current disk usage

    if current_cpu > user_cpu_threshold: 
        print("CPU alert email sent...")
    else:
        print("CPU in safe state")

    if current_memory > user_memory_threshold:
        print("Memory alert email sent...")
    else:
        print("Memory in safe state")
    
    if current_disk > user_disk_threshold:
        print("Disk usage alert email sent...")

check_system_health()