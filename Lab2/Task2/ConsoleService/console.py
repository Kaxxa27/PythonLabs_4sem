import re

from Task2.UserService.user import User
from Task2.Constants.constants import COMMANDS


class Console:
    def __init__(self):
        pass

    def start(self):
        authorization = False
        self.print_command()
        login = "Guest"
        while True:
            try:
                command = input(f"[{login}] --> Enter command: ")
            except KeyboardInterrupt:
                if authorization:
                    check_answer("\nWant to save storage before you go out? [Yes/No]: ", user.save_storage)
                    break
                else:
                    print("\n*** Exception! ***\nHard exit from the program.")
                    break

            if command == "login":
                authorization = True
                login = input("Enter your login: ")
                if not self.check_login(login):
                    print("Incorrect login was entered.\nOnly letters, numbers and underscores are allowed.")
                    continue
                user = User(login)

                check_answer("Do you want to load a container? [Yes/No]: ", user.load_storage)

            elif command == "help":
                self.print_command()
                continue
            elif command == "exit":
                if authorization:
                    check_answer("\nWant to save storage before you go out? [Yes/No]: ", user.save_storage)
                break

            if authorization:
                if command == "add":
                    count = int(input("Number of elements: "))
                    for index in range(count):
                        user.add_element(input("(add) Enter element: "))
                elif command == "remove":
                    user.remove_element(input("(remove) Enter element: "))
                elif command == "list":
                    user.print_element()
                elif command == "clear":
                    user.storage.clear()
                elif command == "find":
                    user.find_element(input("(find) Enter element: "))
                elif command == "grep":
                    user.find_with_regex(input("(grep) Enter regex: "))
                elif command == "save":
                    user.save_storage()
                elif command == "load":
                    user.load_storage()
                elif command == "switch":
                    check_answer("\nWant to save storage before you go out? [Yes/No]: ", user.save_storage)
                    authorization = False
                    login = "Guest"
                    user.storage.clear()
            else:
                print("You are not registered.\nPlease register by entering the login command.")

    @staticmethod
    def print_command():
        print("Menu:")
        for index in range(len(COMMANDS)):
            print(f"{index + 1}. {COMMANDS[index]}")

    def check_login(self, login):
        return re.fullmatch(r'[a-zA-Z0-9_]+', login)


def check_answer(question, command):
    while True:
        answer = input(question)
        if answer == "Yes":
            command()
            break
        elif answer == "No":
            break
        else:
            print("Wrong input!\nEnter Yes/No please.")
