def check_cpu_usage():
    import psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage is: {cpu_usage}%") 
    if cpu_usage > 75:
        print("Warning: High CPU usage detected!")
    else:  
        print("CPU usage is within normal limits.") 
check_cpu_usage()
# This script checks the current CPU usage and prints a warning if it exceeds 75%.


# This script checks the current Memory usage and prints a warning if it exceeds 80%.
def check_memory_usage():
        import psutil
        memory=psutil.virtual_memory()
        total_gb = memory.total / (1024 ** 3)
        used_gb = memory.used / (1024 ** 3)
        available_gb = memory.available / (1024 ** 3)
        print(f"Total Memory     : {total_gb:.2f} GB")
        print(f"Used Memory      : {used_gb:.2f} GB")
        print(f"Available Memory : {available_gb:.2f} GB")
        print(f"Memory Usage     : {memory.percent}%")
        if memory.percent > 80:
            print("Warning: High Memory usage detected!")
        else:
            print("Memory usage is within normal limits.")      
check_memory_usage()



def check_disk_usage():
        import psutil
        disk=psutil.disk_usage('/')
        total_gb = disk.total / (1024 ** 3)
        used_gb = disk.used / (1024 ** 3)
        free_gb = disk.free / (1024 ** 3)
        print(f"Total Disk Space : {total_gb:.2f} GB")
        print(f"Used Disk Space  : {used_gb:.2f} GB")
        print(f"Free Disk Space  : {free_gb:.2f} GB")
        print(f"Disk Usage       : {disk.percent}%")
        if disk.percent > 85:
                print("Warning: High Disk usage detected!")
        else:
                print("Disk usage is within normal limits.")
check_disk_usage()
# This script checks the current Disk usage and prints a warning if it exceeds 85%.

def check_network_usage():
        import psutil
        net=psutil.net_io_counters()
        bytes_sent_mb = net.bytes_sent / (1024 ** 2)
        bytes_recv_mb = net.bytes_recv / (1024 ** 2)
        print(f"Bytes Sent     : {bytes_sent_mb:.2f} MB")
        print(f"Bytes Received : {bytes_recv_mb:.2f} MB")       
check_network_usage()
# This script checks the current Network I/O statistics and prints the bytes sent and received in MB.