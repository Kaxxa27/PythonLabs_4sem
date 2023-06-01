TEST_INT = [1, 1234566789, -8888, 0]
TEST_FLOAT = [1.2, -6.66666, 1234.455234]
TEST_STR = ["TEST", "test", "{}{}{}{thats}{is}{test}", "<><Base><><><,,,><So><,.>>,,>>><<<Cute>>"]
TEST_BOOL = [True, False]
TEST_NONE = [None]
TEST_COMPLEX = [complex(1, 2), complex(-3, 4), complex(0, -1)]
TEST_LIST = [
    [[], [], []],
    [[1, 2, 3], [4, 5], [6, 7, 8, 9]],
    [[1, 'a', True], ['hello', 2.5], [False, [1, 2, 3]]],
    [[1, 2, 3], [], ['a', '', 'c'], ['', '', '']],
    [[1, 2, 3], [(12, 45, 6)], [4, None, {"123": 123}], [None, None]]
]
TEST_TUPLE = (
    (None, ("str", 0), (1, 2, 34, 5)),
    (1, 2, 34, 56, 7, 8, 8),
    ("Hello", (1, 2, 3), -12992384, complex(1, 2))
)
TEST_SET = [{1, 3, 45, 6, 7, 78, 8}]
TEST_FROZEN_SET = [frozenset({1, 2, 3, 45, 6, 7, "Ho"})]
TEST_BYTES = [b'\x41\x42\x43']
TEST_BYTES_ARRAY = [bytearray(b'\x41\x42\x43')]
TEST_DICT = [
    {
        "1": 1,
        "2": 2,
        "3": 3
    },
    {
        "base":
        {
            "first dict":
                {
                    "second dict":
                        {
                            "third dict":
                                {
                                    "value": 999
                                }
                        }
                }
        }
    },
    {"list": [1, 2, 3], "tuple": (1, 2, 3), "None": None}
]

TEST_GENERATOR = (item for item in range(10))
TEST_LAMBDA = lambda x: x ** 3


def test_closure(sep=" "):
    def inside(string: str):
        return string.strip(sep)

    return inside


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


class A:

    def info(self):
        return "Class A"


class B(A):
    def info(self):
        return "Class B"

class C(B):
    def info(self):
        return 'Class C'


def default_value(x=0, y=0):
    return f"{x} + {y}"





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
        self._name = 'DELETED'

    @classmethod
    def get_const(cls):
        return cls.CONST

    @staticmethod
    def static():
        return 'It is static'
