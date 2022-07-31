from colorama import *
import os

def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def initLog() -> None:
    init()

def info(text: str) -> None:
    print(f"[{Style.BRIGHT}{Fore.YELLOW}i{Style.RESET_ALL}]{text}")

def log(text,success=True) -> None:
    print(f"[{f'{Fore.GREEN}V' if success else f'{Fore.RED}X'}{Style.RESET_ALL}]{text}")

