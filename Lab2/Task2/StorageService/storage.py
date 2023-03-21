class Storage:
    def __init__(self):
        self.storage_set = set()

    def add(self, *key):
        self.storage_set.add(*key)

    def print(self):
        [print(item) for item in self.storage_set]
