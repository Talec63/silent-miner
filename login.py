from webhook import webhook_send
import os, requests, threading, random
from colorama import Fore

scrapy = f"""{Fore.GREEN}  

 ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
       ░    ░           ░    ░  ░   ░     
                                            """

print(scrapy)
#print("")

def option_1():
    print("test")

def menu():
    menu = f"""
    +----------+---------+
    | {Fore.RED}Numerics{Fore.BLUE} | {Fore.RED}Choice{Fore.BLUE} |
    +----------+---------+
    | 1        | MINER   |
    | 2        | DISCORD |
    | 3        | GITHUB  |
    | 4        | Exit    |
    +----------+--------+"""

    print(Fore.BLUE + menu,"\n")

    choice = input(Fore.RED + "> " + Fore.BLUE + "What do you want to do: ")

    if choice == "1":
        option_1()
        #choice = input(Fore.RED + "> " + Fore.BLUE + "What do you want to do: ")


print("")
def login():
    account = input("Did you have an account (y/n): ")

    if account == "y":

        username = input("Username: ")
        password = input("Password: ")

        if username == "Talec" and password == "test":
            print("\nLogin " + Fore.GREEN + "successfully!\n" + Fore.BLUE)

            print("Welcome back", Fore.YELLOW + username,"!")
            menu()



        else:
            print("Bad password!")
    elif account == "n":
        print("Create account")
    else:
        print("\nYou have to reply by yes or no\n")
        login()


login()