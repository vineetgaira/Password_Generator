import string
import argparse
import secrets
import pyperclip

GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = " \033[31m"
RESET = "\033[0m"
BOLD_START = "\033[1m"
BOLD_END = "\033[0m"

def display_menu():
    print(f"{BOLD_START}{BLUE}Welcome! to password generator.{BOLD_END}\n" 
    f"{BLUE}You can generate any type of password of any length.\n"
    "You can use symbols, numbers, letters.\n"
    "You can choose any of the following, and combination, or all of them.\n")
    print(f"{BOLD_START}Select a password strength level.{BOLD_END}\n"
          f"{BLUE}1 : Weak\n" \
          "2 : Meduim\n" \
          f"3 : Strong{RESET}")

def get_user_choice():
    valid_choices=[1,2,3]
    while True:
        try:
            user_choice=int(input(f"{BOLD_START}{BLUE}Enter your choice:{BOLD_END}"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print(f"{RED}Please enter a valid choice! Look at the menu.")
        except ValueError:
            print(f"Please enter a valid choice! Look at the menu.{RESET}")

def password_logic():
    pass
def password_generator():
    pass

display_menu()
get_user_choice()
