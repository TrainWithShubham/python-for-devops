import psutil

def check_system_health():
    cpu_threshodld = input("Enter CPU usage threshold (in percentage): ")
    print("current cpu threshold is : ", cpu_threshodld)

    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU %: ", current_cpu)

    if current_cpu > int(cpu_threshodld):
        print("CPU usage is above the threshold! sending email aert....")
    else:
        print("cpu is in normal state")

check_system_health()