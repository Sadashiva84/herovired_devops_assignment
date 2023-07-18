#This is Question 2 of the assignment
'''
As a DevOps engineer, it is crucial to monitor the health and performance of servers. 
Write a Python program to monitor the health of the CPU. Few pointers to be noted:

●       The program should continuously monitor the CPU usage of the local machine.

●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.

●       The program should run indefinitely until interrupted.

●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

Hint:

●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.

●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

'''
import psutil
import os
from colorama import Fore
from datetime import *

print(Fore.CYAN + "\nSystem Performance Display")

try: # This code tries to look for a timezone module 
    #to print the current time in a certain timezone
    aware_us_central = datetime.now(pytz.timezone('US/Central'))  
    print('US Central DateTime', aware_us_central)  

except: #Since the module is not installed it will gracefully display the message and continue
    print("\n(Timezone Module is Currently Disabled) - Contact administrator to enable")



while True:
    cpu_per = psutil.cpu_percent(2.5)
    ram_per = psutil.virtual_memory()[2]
    print(Fore.YELLOW + f"\nCurrent time {datetime.now()}")
    print(Fore.BLUE + f"\nYour CPU Usage is: {cpu_per} %")
    print(Fore.BLUE + f"Your RAM usage is: {ram_per} %")
    print(Fore.BLUE + f"Number of CPU's is: {os.cpu_count()}")
    
    if cpu_per < 30:
        print(Fore.GREEN + "CPU usage is Very Healthy")
    elif cpu_per > 30 and cpu_per < 70:
        print(Fore.LIGHTYELLOW_EX + "CPU usage is quite Healthy")
    else:
        print(Fore.RED + "Warning!! CPU usage is Unhealthy")



