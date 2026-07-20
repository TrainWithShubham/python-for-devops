import psutil 


# checking usage of CPU
 
def check_cpu_usage():
    cpu_threshold = int(input("Enter the CPU usage threshold (in percentage): "))
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {current_cpu}%")
    if current_cpu > cpu_threshold:
        print(f"Warning: CPU usage is at {current_cpu}%, which exceeds the threshold of {cpu_threshold}%.")
    else:
        print("CPU usage is within the acceptable range.")

# checking usage of disk

def check_disk_usage():
    disk_threshold = int(input("Enter the disk usage threshold (in percentage): "))
    disk_usage = psutil.disk_usage('/').percent
    print(f"Current disk usage: {disk_usage}%")
    if disk_usage > disk_threshold:
        print(f"Warning: Disk usage is at {disk_usage}%, which exceeds the threshold of {disk_threshold}%.")
    else:
        print("Disk usage is within the acceptable range.")

# checking usage of memory

def check_memory_usage():
    memory_threshold = int(input("Enter the memory usage threshold (in percentage): "))
    memory_usage = psutil.virtual_memory().percent
    print(f"Current memory usage: {memory_usage}%")
    if memory_usage > memory_threshold:
        print(f"Warning: Memory usage is at {memory_usage}%, which exceeds the threshold of {memory_threshold}%.")
    else:
        print("Memory usage is within the acceptable range.")   

#Calling the functions to check system health

check_cpu_usage()
check_disk_usage()
check_memory_usage()
