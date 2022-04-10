from colorama import *
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def initLog():
    init()

def info(text):
    print(f"[{Style.BRIGHT}{Fore.YELLOW}i{Style.RESET_ALL}]{text}")

def log(text,success=True):
    print(f"[{f'{Fore.GREEN}V' if success else f'{Fore.RED}X'}{Style.RESET_ALL}]{text}")

