import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter cpu threshold %: "))
    
    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU % : ",current_cpu)
    if current_cpu >= cpu_threshold:
        print("CPU Usage is High, Action required")
    else:
        print("CPU usage is Good, Relax")
        

def check_disk_threshold():
    disk_threshold = int(input("Enter Disk threshold %: "))
    
    current_disk = psutil.disk_usage('/')
    current_percent = current_disk.percent
    print(f"Current Disk Usage: {current_percent}%")
    
    if current_percent >= disk_threshold:
        print("Disk Usage is High, Action required")
    else:
        print("Disk usage is Good, Relax")
        
        
def check_memory_threshold():
    memory_threshold = int(input("Enter Memory threshold %: "))
    
    current_memory = psutil.virtual_memory()
    current_percent = current_memory.percent
    print(f"Current Memory Usage: {current_percent}%")
    
    if current_percent >= memory_threshold:
        print("Memory Usage is High, Action required")
    else:
        print("Memory usage is Good, Relax")                  
        
check_cpu_threshold()
check_disk_threshold()
check_memory_threshold()