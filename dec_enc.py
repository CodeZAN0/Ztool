import os
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
from main import purple
try:
    import uncompyle6
except ImportError:
    os.system("pip install uncompyle6")
logo='''
██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗ 
██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗
██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║
██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║
███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝
╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                   
'''
def decode():
    file=input("FILE : ")
    fs=input("FILE SAVE : ")
    os.system(f"uncompyle6 {file} > {fs}")
    file=open(f"{fs}","a")
    file.write("#decode by LEGEND /n")
    print("DONE DECODE")

def handle_choice(user_choice):
    if user_choice == 1:
        decode()
    elif user_choice == 2:
        print("cooming soon!")
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    while True:
        print(logo)
        print(f'''{purple}
        [01] Decrypter
        [02] Encrypter
        
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
    main()