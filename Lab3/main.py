from pprint import pprint

from json_serializer.json_serializer import JSON_Serializer
from serializer_factory.serializer_factory import Serializer_Factory
class Human:
    CONST = '123ABC456'

    def __init__(self, age, name):
        self._age = age
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age
        self._name = 'name after age deletion'

    @classmethod
    def get_const(cls):
        return cls.CONST

    @staticmethod
    def static():
        return 'It is static'

if __name__ == '__main__':

    json_ser = Serializer_Factory.create_serializer("json")
    json = JSON_Serializer()
    data = 10 + 4j
    file = "Data.txt"

    with open(file, 'w') as f:
        json.dump(data, f)

    with open(file, 'r') as f:
        result = json.load(f)

    pprint(open(file, "r").read())
    pprint(type(result))



