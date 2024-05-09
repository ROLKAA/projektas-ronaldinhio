import json
import random
import os
import time
import string

is_open = True
file_exists = False


def generate_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    all_elem = letters + numbers + symbols
    password = "".join(random.sample(all_elem, length))
    return password


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def delete_password():
    clear_screen()
    print("Please input the website you want to delete.")
    website = input("Website: ")
    if website in data:
        data.pop(website)
        with open("data.json", "w") as new_data_file:
            json.dump(data, new_data_file)
            print("Password deleted successfully")
            time.sleep(3)
    else:
        print("Website not found")
        time.sleep(2)


def view_passwords():
    clear_screen()
    print("Here are your passwords.")
    for website in data:
        print(f"Website: {website}")
        print(f"Username: {data[website]['username']}")
        print(f"Password: {data[website]['password']}")
        print("")
        time.sleep(1)
    input("Press enter to continue...")


try:
    with open("data.json", 'r') as data_file:
        data = json.load(data_file)
        file_exists = True
except FileNotFoundError:
    print("Data.json file was not found. Creating new one...")
    file_exists = False
    time.sleep(3)
    with open("data.json", "w") as data_file:
        json.dump({}, data_file)
    print("Data.json file created.")
    print("Please restart the program.")


def add_password():
    len_pass = 0

    clear_screen()
    try:
        usr_random_password_question = str(input("Do you want a random password? (y/n): "))
        if usr_random_password_question not in ["y", "n"]:
            raise ValueError
        elif usr_random_password_question == "y":
            usr_random_password_question = "y"
        else:
            usr_random_password_question = "n"
    except ValueError:
        print("Invalid input")
        time.sleep(2)
        return

    if usr_random_password_question == "y":
        try:
            len_pass = int(input("How long should password be? (0 for random): "))
            if len_pass < 0:
                raise ValueError
            elif len_pass == 0:
                len_pass = random.randint(8, 20)
            else:
                pass
        except ValueError:
            print("Invalid input")
            time.sleep(2)
            return
    else:
        pass

    print("Please input the following information.")
    website = input("Website: ")
    username = input("Username: ")
    if usr_random_password_question == "y":
        password = generate_password(len_pass)
    else:
        password = input("Password: ")
    with open("data.json", "w") as new_data_file:
        new_data = {website: {"username": username, "password": password}}
        data.update(new_data)
        json.dump(data, new_data_file)
        print("Data added successfully")
        time.sleep(3)
        return


while is_open and file_exists:
    clear_screen()

    print("Welcome to password manager")
    print("1. Add new password")
    print("2. View passwords")
    print("3. Delete password")
    print("4. Exit")
    try:
        command = int(input("Command input (1-4): "))
        if command > 4 or command < 1:
            clear_screen()
            print("Invalid command")
            time.sleep(2)
            continue
    except ValueError:
        clear_screen()
        print("Invalid input")
        time.sleep(3)
        continue

    if command == 1:
        add_password()
    if command == 2:
        view_passwords()
    if command == 3:
        delete_password()
    if command == 4:
        is_open = False