from ConsoleService.console import Console
from StorageService.storage import Storage

def main():
    Main_Console = Console()
    Main_Storage = Storage()

    for i in range(3):
        Main_Storage.add(input(f"{i + 1}. Add in storage: "))

    Main_Storage.print()


    #Main_Console.start()


if __name__ == '__main__':
    main()
