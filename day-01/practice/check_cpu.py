import psutil # import the lib from pypi

# aapko kaam karna hai ki user se CPU threshold lo
# current cpu usage pata karo 
# agar cpu usage threshold se zyada hua, email kar do

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold")) # DONE

    current_cpu = psutil.cpu_percent(interval=1) # DONE
    print("Current CPU %: ",current_cpu)
    if current_cpu > cpu_threshold:  # DONE
        print("CPU Alert Email sent...") # dummy email
    else:
        print("CPU in Safe state...")


check_cpu_threshold()