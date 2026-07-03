import string
import argparse
import secrets
import pyperclip

GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD_START = "\033[1m"
BOLD_END = "\033[0m"

def display_menu():
    print(f"{BOLD_START}{YELLOW}Welcome! to password generator.{BOLD_END}\n" 
    f"{YELLOW}You can genrate any type of password of any length.\n"
    "You can use symbols, numbers, letters.\n"
    "You can choose any of the following, and combination, or all of them.\n")
    print(f"{BOLD_START}Select a password strength level.{BOLD_END}\n"
          f"{YELLOW}1 : Weak\n" \
          "2 : Meduim\n" \
          f"3 : Strong{RESET}")
    


display_menu()
