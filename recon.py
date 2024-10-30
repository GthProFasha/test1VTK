import subprocess
import nmap
from colorama import Fore, Style
from bs4 import BeautifulSoup
import re
import requests
import concurrent.futures
import termcolor

election = input(Fore.BLUE + """\nSelect an option of recon:
            1. Ports
            2. Subdomains
            3. Directories
            4. Vulnerabilities \n""" + Style.RESET_ALL)

if election == "1":
    subprocess.run("clear", shell=True)
    ip = input(Fore.BLUE + "Enter the IP whose ports you wanna scan: " + Style.RESET_ALL)
    portfile = input(Fore.BLUE + "Enter the filename you wanna save the results under: " + Style.RESET_ALL)
    subprocess.run("clear", shell=True)
    subprocess.run(f"nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn {ip} -oN {portfile}", shell=True)
    print(Fore.CYAN + f"The results of {ip} were saved on {portfile}." + Style.RESET_ALL)
    subprocess.run("clear", shell=True)
    subprocess.run("python3 main.py", shell=True)

if election == "2":
    subprocess.run("clear", shell=True)
    url = input(Fore.BLUE + "Enter the URL whose subdomains you wanna scan: " + Style.RESET_ALL)
    subprocess.run("clear", shell=True)
    subprocess.run(f"gobuster vhost -w", shell=True)
    print(Fore.CYAN + f"Here you have the results of {ip}." + Style.RESET_ALL)
    subprocess.run("clear", shell=True)
    subprocess.run("python3 main.py", shell=True)