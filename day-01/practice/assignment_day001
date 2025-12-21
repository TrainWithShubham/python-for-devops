# Day 01 – Introduction to Python for DevOps
# Task
# Today’s goal is to write your first Python script.

# You will create a Python script that:

# Takes threshold values (CPU, disk, memory) from user input
# Also fetches system metrics using a Python library (example: psutil)
# Compares metrics against thresholds
# Prints the result to the terminal
# This is your first step towards thinking like a DevOps engineer using Python.
# Expected Output
# One Python script (example: system_health.py)
# Output should be visible in terminal
# Guidelines
# Use:
# input() for user input
# if / else for decision making
# for loops where required
# Functions to keep the code clean
# Keep the script simple and readable
# Do not over-engineer
# Resources
# Python installation and setup (from live class)
# psutil documentation: https://pypi.org/project/psutil/
# Python basics (inputs, conditions, loops, functions)
# Why This Matters for DevOps
# DevOps engineers frequently write scripts to:

# Check server health
# Validate system conditions
# Generate reports for monitoring and troubleshooting
# This task builds the foundation for automation, monitoring, and reliability.

# Submission
# Fork the repository
# Add your script inside the day-01 folder
# Ensure the script runs successfully
# Commit and push your changes to your fork
# Learn in Public
# Share your progress on LinkedIn:

# Post a small code snippet or a story on how you wrote your first Python Script
# Share the output from the terminal
# Write 2–3 lines on what you learned today (can be a blog article as well)
# Optional:

# Tag TrainWithShubham or Shubham Londhe
# Use hashtags: #PythonForDevOps #TrainWithShubham #DevOpsKaJosh (Helps me to filter post and Like/ Comment / Repost / engage)
# Happy Learning TrainWithShubham


import psutil

# #CPU Threshhold
# def get_cpu_threshold():
#     cpu_threshold = int(input("Enter the CPU Threshold : "))

#     current_cpu = psutil.cpu_percent(interval=1)
#     print("current cpu percentage  :", current_cpu)

#     if current_cpu > cpu_threshold:
#         print("CPU alert email sent...")
#     else:
#         print("CPU is in safe state.")

# get_cpu_threshold()

# #Disk Threshold
# def get_disk_usage():
#     disk_usage = int(input(" Enter the Disk Usage : "))

#     current_disk = psutil.disk_usage('/')
#     print("current disk usage :", current_disk)

#     if current_disk.percent > disk_usage:
#         print("Disk alert email sent...")
#     else:
#         print("Disk is in safe state.")

# get_disk_usage()

# #Memory Threshold
# def get_memory_threshold():
#     memory_threshold = int(input("Enter the Memory Threshold : "))

#     current_memory = psutil.virtual_memory()
#     print("Current Memory Usage :", current_memory)

#     if current_memory.percent > memory_threshold:
#         print("Memory alert email sent...")
#     else:
#         print("Memory is in safe state.")

# get_memory_threshold()


def get_thresholds():
    cpu_threshold = int(input("Enter CPU threshold (%) : "))
    mem_threshold = int(input("Enter Memory threshold (%) : "))
    disk_threshold = int(input("Enter Disk threshold (%) : "))
    return cpu_threshold, mem_threshold, disk_threshold


def check_server_health(cpu_threshold, mem_threshold, disk_threshold):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print("\n----- Server Health Report -----")

    # CPU
    if cpu > cpu_threshold:
        print(f"CPU Usage HIGH : {cpu}%")
    else:
        print(f"CPU Usage OK : {cpu}%")

    # Memory
    if memory > mem_threshold:
        print(f"Memory Usage HIGH : {memory}%")
    else:
        print(f"Memory Usage OK : {memory}%")

    # Disk
    if disk > disk_threshold:
        print(f"Disk Usage HIGH : {disk}%")
    else:
        print(f"Disk Usage OK : {disk}%")


def main():
    cpu_threshold, mem_threshold, disk_threshold = get_thresholds()
    check_server_health(cpu_threshold, mem_threshold, disk_threshold)


if __name__ == "__main__":
    main()



