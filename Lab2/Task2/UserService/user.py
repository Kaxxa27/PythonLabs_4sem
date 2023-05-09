from Task2.StorageService.storage import Storage


class User:
    def __init__(self, name):
        self.name = name
        self.storage = Storage(name)

    def add_element(self, key):
        self.storage.add(key)

    def remove_element(self, key):
        self.storage.remove(key)

    def print_element(self):
        self.storage.list()

    def save_storage(self):
        self.storage.save()

    def load_storage(self):
        self.storage.load()

    def union_storage(self, new_set):
        self.storage.union(new_set)

    def clear_storage(self):
        self.storage.clear()

    def find_with_regex(self, regex):
        self.storage.grep(regex)

    def find_element(self, key):
        self.storage.find(key)
