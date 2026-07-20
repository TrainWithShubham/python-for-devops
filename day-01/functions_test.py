import psutil  
# cpu usage check karne ke liye psutil library ka use karte hai, isko install karne ke liye pip install psutil command ka use karte hai


# Function = "Kamm karna"

# def sum_of_two_numbers():
    
#     num1 = int(input("Enter the first number :"))
#     num2 = int(input("Enter the second number :"))
#     sum = num1+num2
#     print(sum)
# sum_of_two_numbers()



# env = input("Enter the environment : ")
# if env == "Dev":
#     print("Not correct env")
# elif env == "Prod":
#     def sum_of_two_numbers():
    
#         num1 = int(input("Enter the first number :"))
#         num2 = int(input("Enter the second number :"))
#         sum = num1+num2
#         print(sum)
#     sum_of_two_numbers()
# else:
#     print("Please enter correct env")


# env = input("Enter the environment : ")
# if env == "Dev":
#     print("Not correct env")
# elif env == "Prod":
#     sum_of_two_numbers()
# else:
#     print("Please enter correct env")



# cpu_usage = int(input("Enter the CPU usage : "))
# def check_cpu_usage():
#     cpu_usage = int(input("Enter the CPU usage : "))
#     if cpu_usage >= 80:
#         print("Send them an email")
#     else: 
#         print("CPU usage is normal")
# check_cpu_usage()

def check_cpu_usage():
    cpu_threshold = int(input("Enter the CPU threshold : "))
    current_cpu_usage = psutil.cpu_percent(interval=1) # interval = 1 means it will check the CPU usage for 1 second
    print("Current CPU usage is : ", current_cpu_usage)
    if current_cpu_usage > cpu_threshold:
        print("Send them an email")
    else: 
        print("CPU usage is normal")
check_cpu_usage()