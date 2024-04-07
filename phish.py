import os
from mimetypes import init
from termcolor import colored
import requests
from email import message
import colorama
from colorama import Back, Fore, Style
import sys
import time


colorama.init(autoreset=True)

# color frontend
fred = Fore.RED
fgreen = Fore.GREEN
flm = Fore.LIGHTMAGENTA_EX
fblue = Fore.BLUE
fyellow = Fore.YELLOW
fly = Fore.LIGHTYELLOW_EX
fwhite = Fore.WHITE
fcyan = Fore.CYAN
fblack = Fore.BLACK



#Vip color
black ="\033[0;30m"
red ="\033[0;31m"
bred ="\033[1;31m"
green ="\033[0;32m"
vgreen ="\033[1;32m"
yellow ="\033[0;33m"
vyellow ="\033[1;33m"
blue ="\033[0;34m"
vblue ="\033[1;34m"
purple ="\033[0;35m"
bpurple ="\033[1;35m"
cyan ="\033[0;36m"
vcyan ="\033[1;36m"
white ="\033[0;37m"
nc ="\033[00m"

# Backend color
br = Back.RED
bw = Back.WHITE
bg = Back.GREEN
bb = Back.BLUE
bly = Back.LIGHTYELLOW_EX
bblack = Back.BLACK


logo = ''' 
▒███████▒ ▄▄▄       ███▄    █  ██ ▄█▀ ▒█████      ██▓    ▓█████   ▄████ ▓█████  ███▄    █ ▓█████▄ 
▒ ▒ ▒ ▄▀░▒████▄     ██ ▀█   █  ██▄█▒ ▒██▒  ██▒   ▓██▒    ▓█   ▀  ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
░ ▒ ▄▀▒░ ▒██  ▀█▄  ▓██  ▀█ ██▒▓███▄░ ▒██░  ██▒   ▒██░    ▒███   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒░██   █▌
  ▄▀▒   ░░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██ █▄ ▒██   ██░   ▒██░    ▒▓█  ▄ ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
▒███████▒ ▓█   ▓██▒▒██░   ▓██░▒██▒ █▄░ ████▓▒░   ░██████▒░▒████▒░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▓ 
░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒░▒░▒░    ░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
░░▒ ▒ ░ ▒  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒ ▒░  ░ ▒ ▒░    ░ ░ ▒  ░ ░ ░  ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
░ ░ ░ ░ ░  ░   ▒      ░   ░ ░ ░ ░░ ░ ░ ░ ░ ▒       ░ ░      ░   ░ ░   ░    ░      ░   ░ ░  ░ ░  ░ 
  ░ ░          ░  ░         ░ ░  ░       ░ ░         ░  ░   ░  ░      ░    ░  ░         ░    ░    
░                                                                                          ░      
coded by :zano1'''



def phish():
    file = open('\PyPhisher-main/pyphisher')
    print(file)







def handle_choice(user_choice):
    if user_choice == 1:
        phish()
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
    elif user_choice == 14:
        print("cooming soon!")
    elif user_choice == 15:
        print("cooming soon!")
    elif user_choice == 16:
        print("cooming soon!")
    elif user_choice == 17:
        print("cooming soon!")
    elif user_choice == 18:
        print("cooming soon!")
    elif user_choice == 19:
        print("cooming soon!")
    elif user_choice == 20:
        print("cooming soon!")
    elif user_choice == 21:
        print("cooming soon!")
    elif user_choice == 22:
        print("cooming soon!")
    elif user_choice == 23:
        print("cooming soon!")
    elif user_choice == 24:
        print("cooming soon!")
    elif user_choice == 25:
        print("cooming soon!")
    elif user_choice == 26:
        print("cooming soon!")
    elif user_choice == 27:
        print("cooming soon!")
    elif user_choice == 28:
        print("cooming soon!")
    elif user_choice == 29:
        print("cooming soon!")
    elif user_choice == 00:
        print("cooming soon!")
    elif user_choice == 99:
       print("cooming soon!")
    elif user_choice == 000:
        print("cooming soon!")
    else:
        print(Fore.RED + "Invalid choice. Please select a valid option.")

def menuphish():
    while True:
        print(logo)

        print(f'''{purple}
        [01] Pyphisher                    [14] Website Tools
        [02] IP                           [15] Ddos Attacke
        [03] Checker                      [16] Bypass
        [04] Generator                    [17] Bomber
        [05] Informaiton                  [18] spamming
        [06] Delete Files From Folder     [19] decrypter & encrypter
        [07] Combo                        [20] Exploit
        [08] Back Door                    [21] Scraping
        [09] Phishing Tool                [22] coming soon
        [10] Brute Force                  [23] coming soon                      
        [13] Cracker                      [24] Other Tool

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
    main1()