# Created by Gth

import subprocess
from colorama import Fore, Style
from bs4 import BeautifulSoup
import re
import requests
import concurrent.futures
import termcolor

def logo():
    print(Fore.LIGHTRED_EX + """
###                           ###
 ###                         ###
  ###                       ###
   ###                     ###
    ###                   ###
     ###                 ###
      ###               ###
       ###             ###
        ###           ###   
         ###         ###
          ###       ###
           ###     ###
            ###   ###
             ### ###
              #####
               ###
""" + Style.RESET_ALL)
    print(Fore.GREEN + "Created by" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + "Gth" + Style.RESET_ALL)
    ()

logo()

election = input(Fore.BLUE + """\nSelect an option:
            1. Recon
            2. Crack passwords/hashes
            3. Exploit / Advanced Recon
            4. ??? (for this one, enter code 242) \n""" + Style.RESET_ALL)

if election == "1":
    def recon():
        subprocess.run("clear", shell=True)
        subprocess.run("sudo python3 recon.py", shell=True)
    ()

elif election == "2":
    def crack():
        subprocess.run("clear", shell=True)
        subprocess.run("sudo python3 crack.py", shell=True)
    ()

elif election == "3":
    def exploit():
        subprocess.run("clear", shell=True)
        subprocess.run("sudo python3 exploit.py", shell=True)
    ()

elif election == "4":
    def almost():
        subprocess.run("clear", shell=True)
        print(Fore.LIGHTRED_EX + "Upss! Try with the correct code to get this option! ;)" + Style.RESET_ALL)
    ()

elif election == "242":
    def scrt():
        subprocess.run("clear", shell=True)
        print(Fore.LIGHTRED_EX + "Alright, this is gonna be dark..." + Style.RESET_ALL)
        subprocess.run("python3 scrt.py", shell=True)
    ()

else:
    print(Fore.LIGHTRED_EX + "Please, select a valid option." + Style.RESET_ALL)
    subprocess.run("clear", shell=True)
    subprocess.run("sudo python3 main.py", shell=True)
