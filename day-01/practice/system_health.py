import psutil


def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold value: "))

    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU %: ",current_cpu)
    if current_cpu > cpu_threshold: 
        print("CPU Alert Email sent...")
    else:
        print("CPU in Safe state...")


def check_cpu_disc_space():
    disc_threshold = int(input("Enter the CPU Threshold value: "))
    current_disc = psutil.disk_usage('/')
    print("Current Disc %: ",current_disc)
    used_percentage = current_disc.percent

    print("Current Disc %: ",used_percentage)
    if used_percentage > disc_threshold:
        print("Disk Alert Email sent...")
    else:
        print("Disk in Safe state...")
    


def check_memory():
    memory_threshold = int(input("Enter the Momory Threshold value: ")) 
    current_memory = psutil.virtual_memory()
    used_memory_percentage = current_memory.percent
    print("Current Memory %: ",used_memory_percentage)

    if used_memory_percentage > memory_threshold:
        print("Memory Alert Email sent...")
    else:
        print("Memory in Safe state...")



check_cpu_threshold()
check_cpu_disc_space()
check_memory()
