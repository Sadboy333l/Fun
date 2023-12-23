import os
from time import sleep 
from colorama import Fore, Style

#clear command
os.system('clear')

#head 
print(f"{Fore.GREEN}################################### {Style.RESET_ALL}")
print(f"{Fore.GREEN}|            WELCOME              | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|                                 | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|            Age Test             | {Style.RESET_ALL}")                     print(f"{Fore.GREEN}|                                 | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|                                 | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|---------------------------------| {Style.RESET_ALL}")
print(f"{Fore.GREEN}|                                 | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|   Creator:  Aria....            | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|                                 | {Style.RESET_ALL}")
print(f"{Fore.GREEN}|                                 | {Style.RESET_ALL}")                     print(f"{Fore.GREEN}################################### {Style.RESET_ALL}")

#enter your age 
age = input("your Age: ")

#loading
l = ["working 18%...", "working 22%....", "working 25%.....", "working 30%......", "working 37%.......", "working 46%........", "working 55%..........""working 69%..........", "working 76%...........","working 89%.............", "working 99%............." ]

#speed loading 
for i in l:
    print("\r" + i, end="")
    sleep(1.6)
print()

#print age 
print(f"{Fore.RED}Your Age is: {Style.RESET_ALL} => {age}")

#Finish:
Brake = input("Press Enter to Continue...")
print("Enjoy :) ")
