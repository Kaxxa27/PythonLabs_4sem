from Task2.StorageService.fileservice import create_filename, save_to_file, load_from_file, check_file
import re


class Storage:
    def __init__(self, filename):
        self.path = create_filename(filename)
        self.storage_set = set()

    def add(self, key):
        self.storage_set.add(key)

    def remove(self, key):
        if key in self.storage_set:
            self.storage_set.remove(key)
        else:
            print("The element is missing.")

    def list(self):
        [print(item) for item in self.storage_set]

    def save(self):
        save_to_file(self.path, list(self.storage_set))

    def load(self):
        if check_file(self.path):
            self.union(set(load_from_file(self.path)))
        else:
            print("You don't have any saved files yet.\nUse the save command.")

    def union(self, new_set):
        self.storage_set = self.storage_set.union(new_set)

    def grep(self, regex):
        check = False
        print("Searching elements...")
        for index in range(len(self.storage_set)):
            if re.fullmatch(fr"{regex}", list(self.storage_set)[index]):
                check = True
                print(list(self.storage_set)[index])
        if not check:
            print("No such elements.")

    def clear(self):
        self.storage_set.clear()

    def length(self):
        return len(self.storage_set)

    def find(self, key):
        check = False
        print("Searching elements...")
        if key in self.storage_set:
            print(key)
            check = True
        if not check:
            print("No such elements.")
