import psutil # import the lib from pypi

def check_cpu_usage():
    user_cpu = int(input("Enter the CPU Threhold \n"))

    current_cpu = psutil.cpu_percent(interval=1) # check current cpu
    print("current cpu usage % ",current_cpu)

    if current_cpu > user_cpu:
        print("cpu alert email sent...")
    else:
        print("cpu in safe state")

check_cpu_usage()

#print(dir(psutil))
