import string
import argparse
import secrets
import pyperclip

GREEN = "\033[32m"
BLUE = "\033[34m"
RED = " \033[31m"
RESET = "\033[0m"
BOLD_START = "\033[1m"
BOLD_END = "\033[0m"
MAX_LENGTH = 64
MIN_LENGTH = 1
WEAK = (string.ascii_lowercase + string.ascii_uppercase)
MEDIUM = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
STRONG = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)





def display_menu():
    print(f"{BOLD_START}{BLUE}Welcome! to password generator.{BOLD_END}\n" 
    f"{BLUE}You can generate any type of password of any length.\n"
    "You can use symbols, numbers, letters.\n"
    "You can choose any of the following, and combination, or all of them.\n")
    print(f"{BOLD_START}Select a password strength level.{BOLD_END}\n"
          f"{BLUE}1 : Weak(only letters)\n" \
          "2 : Medium(letters + numbers)\n" \
          f"3 : Strong(letters + numbers + symbols){RESET}")

def get_user_choice():
    valid_choices={1,2,3}
    while True:
        try:
            length=int(input(f"{BOLD_START}{BLUE}Enter the length of the password(integer):{BOLD_END}"))
            if not (MIN_LENGTH <= length <= MAX_LENGTH):
                print(f"{RED}Please enter a valid choice! Between 1-64.")
                continue
        except ValueError:
            print(f"{RED}Please enter a integer between 1-64.{RESET}")
            continue
        while True:
            try:
                user_choice=int(input(f"{BOLD_START}{BLUE}Enter your choice:{BOLD_END}"))
                if user_choice in valid_choices:
                    return user_choice, length
                else:
                    print(f"{RED}Please enter a valid choice! Look at the menu.")
            except ValueError:
                print(f"{RED}Please enter a valid choice! Look at the menu.{RESET}")
        
def password_logic():
    password = ""
    user_choice,length=get_user_choice()
    if user_choice==1:
        for _ in range(length):
            password += secrets.choice(WEAK)
        return password
    elif user_choice==2:
        for _ in range(length):
            password += secrets.choice(MEDIUM)
        return password
    elif user_choice==3:
        for _ in range(length):
            password += secrets.choice(STRONG)
        return password
        
def password_generator():
    pass

def display_password():
    pass
def copy_to_clipboard():
    pass


                

