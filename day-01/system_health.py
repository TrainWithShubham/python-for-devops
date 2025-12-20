import psutil

def cpu_check():
    cpu_threshold = int(input("Enter the threshold for cpu: "))

    current_cpu = psutil.cpu_percent(interval=1)
    print(current_cpu)
    if (current_cpu > cpu_threshold):
        print("Current CPU usage is high")
    else:
        print("Current CPU usage is normal")

def memory_check():
    memory_threshold = int(input("Enter the threshold for memory: "))

    current_memory = psutil.virtual_memory().percent
    print(current_memory)
    if (current_memory > memory_threshold):
        print("Memory uage is high")
    else:
        print("Memory usage is normal")

def disk_check():
    disk_threshold = int(input("Enter the threshold for disk: "))
    def disk(drive):
        current_disk = psutil.disk_usage(drive).percent
        print(current_disk)
        if (current_disk > disk_threshold):
            print(f"Disk usage for {drive} drive is high")
        else:
            print(f"Disk usage for {drive} drive is normal")
    disk(drive='C:')
    disk(drive='D:')

cpu_check()
memory_check()
disk_check()