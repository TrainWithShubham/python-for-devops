import psutil

# Taking threshold values from user
cpuThreshold = int(input("Enter CPU threshold: "))
diskThreshold = int(input("Enter disk threshold: "))
memThreshold = int(input("Enter memory threshold: "))

# Check System Health
def checkSystemHealth(cpuThreshold,diskThreshold,memThreshold):

  # Fetch System Metrics
  cpuUsage = psutil.cpu_percent(interval=1)
  diskUsage = psutil.disk_usage('/').percent
  memUsage = psutil.virtual_memory().percent

  print("\n-- System Health Check --")

  # CPU check
  if(cpuUsage>cpuThreshold):
    print(f"⚠️ CPU usage High: {cpuUsage}% (Threshold:{cpuThreshold}%)")
  else:
    print(f"✅ CPU usage OK: {cpuUsage}%")

  # Disk check
  if(diskUsage>diskThreshold):
    print(f"⚠️ Disk usage High: {diskUsage}% (Threshold:{diskThreshold}%)")
  else:
    print(f"✅ Disk usage OK: {diskUsage}%")

  # Memory check
  if(memUsage>memThreshold):
    print(f"⚠️ Memory usage High: {memUsage}% (Threshold:{memThreshold}%)")
  else:
    print(f"✅ Memory usage OK: {memUsage}")

for i in range(5):
  checkSystemHealth(cpuThreshold,diskThreshold,memThreshold)