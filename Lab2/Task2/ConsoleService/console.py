class Console:
    def __init__(self):
        pass

    def start(self):
        while True:
            print("Menu:")
            print("1. print:")
            print("2. exit:")
            command = input("Enter command: ")
            if command == "print":
                print(self.print_str())
            if command == "exit":
                break

    def print_str(self):
        return input("Enter string: ")
