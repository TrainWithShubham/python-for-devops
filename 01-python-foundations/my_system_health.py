import psutil

try:
    threshold = input("Enter the CPU threshold (%): ")
    threshold = float(threshold)
except ValueError:
    print("That's not a valid number. Please enter something like 75 or 80.5")
    exit()

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("/").percent

print("You entered:", threshold)
print("Current CPU usage:", cpu_usage)
print("Current Memory usage:", memory_usage)
print("Current Disk usage:", disk_usage)

if cpu_usage > threshold:
    print("CPU status: WARNING - usage is above threshold")
else:
    print("CPU status: Healthy")

if memory_usage > threshold:
    print("Memory status: WARNING - usage is above threshold")
else:
    print("Memory status: Healthy")

if disk_usage > threshold:
    print("Disk status: WARNING - usage is above threshold")
else:
    print("Disk status: Healthy")