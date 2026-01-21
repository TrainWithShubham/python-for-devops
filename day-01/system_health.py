#pyscipt to Check CPU Usages

import psutil

def check_cpu_usages(name,usages,limit):
    if usages > limit:
        print("CPU alert email Send High Use...")
    else:
        print("Usages is Ok")    

cpu_limit = int(input("Enter CPU Threshold"))
memory_limit = int(input("Enter Memory Threshold"))
disk_limit = int(input("Enter Disk Threshhold"))

print("\n Checking Systems Usages...")

cpu_usage = psutil.cpu_percent(1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

check_cpu_usages("CPU", cpu_usage, cpu_limit)

check_cpu_usages("Memory", memory_usage, memory_limit)

check_cpu_usages("Disk", disk_usage, disk_limit)