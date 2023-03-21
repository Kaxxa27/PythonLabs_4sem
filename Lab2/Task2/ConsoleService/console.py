from Task2.UserService.user import User


class Console:
    def __init__(self):
        pass

    def start(self):
        authorization = False
        self.print_command()

        while True:
            command = input("Enter command: ")
            if command == "login":
                authorization = True
                login = input("Enter your login: ")
                user = User(login)

                while True:
                    answer = input("Do you want to load a container? [Yes/No]: ")
                    if answer == "Yes":
                        user.load_storage()
                        break
                    elif answer == "No":
                        break
                    else:
                        print("Wrong input!\nEnter Yes/No please.")
            if command == "help":
                self.print_command()
                continue
            if command == "exit":
                break
            if authorization:
                if command == "add":
                    user.add_element(input("(add) Enter element: "))
                if command == "remove":
                    user.remove_element(input("(remove) Enter element: "))
                if command == "list":
                    user.print_element()
                if command == "find":
                    user.find_element(input("(find) Enter element: "))
                if command == "grep":
                    user.find_with_regex(input("(grep) Enter regex: "))
                if command == "save":
                    user.save_storage()
                if command == "load":
                    user.load_storage()
            else:
                print("You are not registered.\nPlease register by entering the login command.")

    def print_command(self):
        print("Menu:")
        print("1. login:")
        print("2. add: ")
        print("3. remove: ")
        print("4. find: ")
        print("5. grep: ")
        print("6. save: ")
        print("7. load: ")
        print("8. help: ")
        print("9. list: ")
        print("10. exit: ")
