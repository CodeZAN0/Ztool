import os
from mimetypes import init
from termcolor import colored
import requests
import colorama
from colorama import Back, Fore, Style
import sys
import time
import subprocess
from logo import logo, clear

colorama.init(autoreset=True)
purple ="\033[0;35m"




def handle_choice(user_choice):
    if user_choice == 1:
        from f import main
        main()
    elif user_choice == 2:
        print("cooming soon!")
    elif user_choice == 3:
        print("cooming soon!")
    elif user_choice == 4:
        print("cooming soon!")
    elif user_choice == 5:
        print("cooming soon!")
    elif user_choice == 6:
        print("cooming soon!")
    elif user_choice == 7:
        print("cooming soon!")
    elif user_choice == 8:
        print("cooming soon!")
    elif user_choice == 9:
        print("cooming soon!")
    elif user_choice == 10:
        print("cooming soon!")
    elif user_choice == 11:
        print("cooming soon!")
    elif user_choice == 12:
        print("cooming soon!")
    elif user_choice == 13:
        print("cooming soon!")
    elif user_choice == 99:
        clear()
    elif user_choice == 000:
        print("cooming soon!")
    else:
        print(Fore.RED + "Invalid choice. Please select a valid option.")

def smmenu():
    while True:
        print(logo)

        print(f'''{purple}
        [01] auto like,delete post ect... 
        [02] telegram kit , send message  , info bot     
        [03]             
        [04]                  
        [05]                    
        [06]       
        [07]                        
        [08]                   
        [09]                  
        [10]                                      
        [13]                       

        [99] Clear         [0] Exit       [000] About
        ''')


        try:
            user_choice = int(input(Fore.YELLOW + "Enter your choice: "))
        except ValueError:
            print(Fore.YELLOW + "Invalid input. Please enter a number.")
            continue

        if user_choice == 0:
            print(Fore.YELLOW + "Exiting the program. Goodbye!")
            break

        handle_choice(user_choice)

if __name__ == "__main__":
    smmenu()