import webbrowser
import requests
import pyfiglet
from colorama import Fore, init
import csv
init(autoreset=True)

banner = pyfiglet.figlet_format("SnapSearch")
print(Fore.YELLOW + banner)

def single_lookup():
    username = input("Enter a username: ")
    print()
    check_snap = "https://feelinsonice.appspot.com/web/deeplink/snapcode?username={}&size=400&type=SVG".format(username)
    verify_snap = "https://snapchat.com/add/{}".format(username)
    r = requests.get(check_snap)

    if "image clip" in r.text:
        print(Fore.GREEN + "[+] " + Fore.WHITE + " Snapchat found!")
        print()
        verify = input("Do you want to verify? " + Fore.RED + "(y/n) " + Fore.WHITE)
        print()
        if verify == "y":
            webbrowser.open(verify_snap)
        else:
            exit()
    else:
        print(Fore.RED + "[+] " + Fore.WHITE + "Snapchat can't be found.")
        print()

def csv_lookup():
    f = open("snapsearch.csv")
    csv_f = csv.reader(f)

    for row in csv_f:
        row = "".join(row)
        check_snap = "https://feelinsonice.appspot.com/web/deeplink/snapcode?username={}&size=400&type=SVG".format(row)
        verify_snap = "https://snapchat.com/add/{}".format(row)
        r = requests.get(check_snap)
        if "image clip" in r.text:
            print(Fore.BLUE + row + Fore.GREEN + " [+] " + Fore.WHITE + "Snapchat found!")
        else:
            print(Fore.BLUE + row + Fore.RED + " [-] " + Fore.WHITE + "Snapchat not found.")
    print()

print(Fore.YELLOW + "[1] " + Fore.WHITE + "Look up a single username")
print(Fore.YELLOW + "[2] " + Fore.WHITE + "Look up from csv")
print()
option = input("Select an option: ")
print()

if option == "1":
    single_lookup()
elif option == "2":
    csv_lookup()
