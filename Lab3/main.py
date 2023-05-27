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


def test(sep=" "):
    def inside(string: str):
        return string.strip(sep)
    return inside


if __name__ == '__main__':
    factory = Serializer_Factory()
    json_ser = factory.create_serializer("json")
    xml_ser = factory.create_serializer("xml")
    data = Human(12,"Jeka")
    file = "Data.txt"

    with open(file, 'w') as f:
        xml_ser.dump(data, f)

    with open(file, 'r') as f:
        result = xml_ser.load(f)

    pprint(open(file, "r").read())
    pprint(type(result))
    # pprint(list(result))

    # test = result()
    # pprint(test("Jeak sdfs f      "))




# import math
# from pprint import pprint
#
# from json_serializer.json_serializer import JSON_Serializer
#
#
# class A:
#     def my_method(self):
#         return 5
#
#
# class B:
#     def another_method(self):
#         return 6
#
#
# class C(A, B):
#     pass
#
#
# x = 10
#
#
# def my_func(a):
#     return math.sin(x * a)
#
#
# json_ser = JSON_Serializer()
# obj = C()
# ser_obj = json_ser.dumps(obj)
# deser_obj = json_ser.loads(ser_obj)
# pprint(deser_obj.my_method())  # returns 5
# pprint(deser_obj.another_method())  # returns 6
#
# ser_class = json_ser.dumps(C)
# deser_class = json_ser.loads(ser_class)
# obj = deser_class()
# pprint(obj.my_method())   # returns 5
# pprint(obj.another_method())   # returns 6
#
# ser_func = json_ser.dumps(my_func)
# deser_func = json_ser.loads(ser_func)
# pprint(deser_func(20))   # returns sin(10 * 20)
