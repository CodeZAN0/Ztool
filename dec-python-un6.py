import os
try:
    import uncompyle6
except ImportError:
    os.system("pip install uncompyle6")
logo='''

███▄ ▄███▓ ██▀███  ▒██   ██▒   
▓██▒▀█▀ ██▒▓██ ▒ ██▒▒▒ █ █ ▒░   
▓██    ▓██░▓██ ░▄█ ▒░░  █   ░   
▒██    ▒██ ▒██▀▀█▄   ░ █ █ ▒    
▒██▒   ░██▒░██▓ ▒██▒▒██▒ ▒██▒   
░ ▒░   ░  ░░ ▒▓ ░▒▓░▒▒ ░ ░▓ ░   
░  ░      ░  ░▒ ░ ▒░░░   ░▒ ░   
░      ░     ░░   ░  ░    ░     
       ░      ░      ░    ░     
           YOUTUBE : MRX CODER
           TELEGRAM : i4m_mrx
           SNAPCHAT : mrx_coder                                

'''
def mrxcoder():
    print(logo)
    halo=input("FILE : ")
    mrx=input("FILE SAVE : ")
    os.system(f"uncompyle6 {halo} > {mrx}")
    file=open(f"{mrx}","a")
    file.write("#decode by mrxcoder /n")
    print("DONE DECODE")
mrxcoder()