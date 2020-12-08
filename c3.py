# c3

import os
import sys
import time
from colorama import Fore

def __admin__():
    os.system("clear")
    try:
        time.sleep(2)
        print("Hello Welcome To The Panel Admin ;)")
        time.sleep(2)
        sec = input(Fore.GREEN + "\n[!] - Enter The Security Name ==> " + Fore.BLACK + "  ")
        if sec != "<hi>":
            try:
                time.sleep(2)
                print(Fore.RED + "\n[!] ~ Your Name Admin Is Not Found ;(")
                time.sleep(2)
                sys.exit()
            except:
                pass
        if sec == "<hi>":
            try:
                time.sleep(2)
                print(Fore.GREEN + "\n[+] ~ Your Name Admin Is Ok ;)")
                time.sleep(2)
                num = input(Fore.GREEN + "\n[!] ~ Enter Your Ramz Admin ==> " + Fore.BLACK + "  ")
                if num != "4030":
                    try:
                        time.sleep(2)
                        print(Fore.RED + "\n[!] - Your Ramz Is Not Fount ;(")
                        time.sleep(2)
                        sys.exit()
                    except:
                        pass
                if num == "4030":
                    try:
                        print(Fore.GREEN + "[+] ~ Your Ramz Is Ok ;)")
                        time.sleep(2)
                        print(Fore.RED + "\n[*] ~ The 5 Sec Go To The Panel Admin ;)")
                        time.sleep(2)
                        print(Fore.RED + "WebSite : " + Fore.BLUE + "https://github.com/")
                        time.sleep(1)
                        print(Fore.RED + "\nUserName : " + Fore.BLUE + "mohammad373")
                        time.sleep(1)
                        print(Fore.RED + "PassWord : " + Fore.BLUE + "0990m0990")
                        time.sleep(2)
                        print(Fore.YELLOW + "\n[*] ~ Good Lunch Admin ;)")
                        sys.exit()
                    except:
                        pass
            except:
                pass
    except:
        pass
__admin__()
