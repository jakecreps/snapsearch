import webbrowser
import requests
import pyfiglet
from colorama import Fore, init
init(autoreset=True)

banner = pyfiglet.figlet_format("SnapSearch")
print(Fore.YELLOW + banner)
username = input("Enter a username: ")
check_snap = "https://feelinsonice.appspot.com/web/deeplink/snapcode?username={}&size=400&type=SVG".format(username)
verify_snap = "https://snapchat.com/add/{}".format(username)
r = requests.get(check_snap)

if "image clip" in r.text:
    print(Fore.YELLOW + "[!] Snapchat Exists!")
    verify = input("Do you want to verify? " + Fore.RED + "(y/n) " + Fore.WHITE)
    if verify == "y":
        webbrowser.open(verify_snap)
    else:
        exit()
else:
    print("Snapchat Doesn't Exist!")
