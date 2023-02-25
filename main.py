import os, colorama, requests, time
from colorama import Fore, init

import sys

sys.stdout.write("\x1b]2; Home V1 Home Holder!\x07")

banner = f"""
██╗  ██╗ ██████╗ ███╗   ███╗███████╗    ██╗   ██╗ ██╗
██║  ██║██╔═══██╗████╗ ████║██╔════╝    ██║   ██║███║
███████║██║   ██║██╔████╔██║█████╗      ██║   ██║╚██║
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝      ╚██╗ ██╔╝ ██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗     ╚████╔╝  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝      ╚═══╝   ╚═╝
 ╔══════════════════════════════════════════════════╦ 
 ║   Welcome To Home V1 this is a home-holder       ║
 ║   ============================================   ║
 ║   Please type 'Methods' to see our methods       ║
 ╚══════════════════════════════════════════════════╝

"""

methods = f"""
██╗  ██╗ ██████╗ ███╗   ███╗███████╗    ██╗   ██╗ ██╗
██║  ██║██╔═══██╗████╗ ████║██╔════╝    ██║   ██║███║
███████║██║   ██║██╔████╔██║█████╗      ██║   ██║╚██║
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝      ╚██╗ ██╔╝ ██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗     ╚████╔╝  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝      ╚═══╝   ╚═╝
 ╔════════════════════════════════════════════╦ 
 ║   Home Holder V1 - Home-Hold methods!      ║
 ║   ======================================   ║
 ║             Home-Hold                      ║
 ╚════════════════════════════════════════════╝
"""


def login():
  user = input(f'{Fore.LIGHTRED_EX}User: ')
  password = input(f'{Fore.LIGHTRED_EX}Pass: ')
  f = open('users.txt', 'r')
  check = f.read()
  if user and password in check:
    main()
  else:
    print('Invalid User & password!')


def main():
  os.system('clear')
  print(banner)

  choice = input(f'{Fore.CYAN}[home@guest]$ ')
  if choice == "Methods":
    os.system('clear')
    print(methods)
    time.sleep(3.4)
    os.system('clear')
    main()

  if choice == "homehold":
    os.system('clear')
    print(banner)
    ip = input(f'{Fore.RED} ip:')
    os.system(f'perl dos.pl {ip}')
    main()
  else:
    os.system('clear')
    main()


login()
