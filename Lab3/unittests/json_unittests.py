import types
import unittest
from json_serializer.json_serializer import JSON_Serializer
from unittests.code_for_tests import (
    TEST_INT, TEST_FLOAT, TEST_STR,
    TEST_BOOL, TEST_SET, TEST_DICT,
    TEST_LIST, TEST_BYTES,
    TEST_TUPLE, TEST_LAMBDA, TEST_COMPLEX,
    TEST_GENERATOR, TEST_BYTES_ARRAY, TEST_FROZEN_SET,
    Human, A, B, C, test_closure, default_value, factorial
)


class BaseJsonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer = JSON_Serializer()
        self.alias = lambda x: self.serializer.loads(self.serializer.dumps(x))


class BasePrimitiveTestCase(BaseJsonTestCase):
    def test_int(self):
        for element in TEST_INT:
            # print(self.serializer.dumps(element))
            self.assertIsInstance(self.alias(element), int)
            self.assertEqual(element, self.alias(element))

    def test_float(self):
        for element in TEST_FLOAT:
            self.assertIsInstance(self.alias(element), float)
            self.assertEqual(element, self.alias(element))

    def test_bool(self):
        for element in TEST_BOOL:
            self.assertIsInstance(self.alias(element), bool)
            self.assertEqual(element, self.alias(element))

    def test_str(self):
        for element in TEST_STR:
            self.assertIsInstance(self.alias(element), str)
            self.assertEqual(element, self.alias(element))

    def test_none(self):
        self.assertEqual(None, self.alias(None))

    def test_complex(self):
        for element in TEST_COMPLEX:
            self.assertIsInstance(self.alias(element), complex)
            self.assertEqual(element, self.alias(element))


class CollectionsTestCase(BaseJsonTestCase):
    def test_list(self):
        for element in TEST_LIST:
            self.assertIsInstance(self.alias(element), list)
            self.assertEqual(element, self.alias(element))

    def test_set(self):
        for element in TEST_SET:
            self.assertIsInstance(self.alias(element), set)
            self.assertEqual(element, self.alias(element))

    def test_frozenset(self):
        for element in TEST_FROZEN_SET:
            self.assertIsInstance(self.alias(element), frozenset)
            self.assertEqual(element, self.alias(element))

    def test_bytes(self):
        for element in TEST_BYTES:
            self.assertIsInstance(self.alias(element), bytes)
            self.assertEqual(element, self.alias(element))

    def test_bytes_array(self):
        for element in TEST_BYTES_ARRAY:
            self.assertIsInstance(self.alias(element), bytearray)
            self.assertEqual(element, self.alias(element))

    def test_dict(self):
        for element in TEST_DICT:
            self.assertIsInstance(self.alias(element), dict)
            self.assertEqual(element, self.alias(element))

    def test_tuple(self):
        for element in TEST_TUPLE:
            self.assertIsInstance(self.alias(element), tuple)
            self.assertEqual(element, self.alias(element))


class FunctionTestCase(BaseJsonTestCase):
    def test_factorial(self):
        self.assertIsInstance(self.alias(factorial), types.FunctionType)
        self.assertEqual(24, self.alias(factorial)(4))
        self.assertEqual(120, self.alias(factorial)(5))

    def test_def_value(self):
        self.assertIsInstance(self.alias(default_value), types.FunctionType)
        self.assertEqual("1 + 2", self.alias(default_value)(1, 2))
        self.assertEqual("Hi + 2", self.alias(default_value)("Hi", 2))
        self.assertEqual("100 + 444", self.alias(default_value)(100, 444))

    def test_lambda(self):
        self.assertIsInstance(self.alias(TEST_LAMBDA), types.LambdaType)
        self.assertEqual(125, self.alias(TEST_LAMBDA)(5))
        self.assertEqual(1000000, self.alias(TEST_LAMBDA)(100))

    def test_closure(self):
        self.assertIsInstance(self.alias(test_closure), types.LambdaType)
        self.assertEqual("TEST", self.alias(test_closure)()("TEST         "))
        self.assertEqual("Hello, World!", self.alias(test_closure)()("                  Hello, World!            "))

    def test_generator(self):
        test_gen = self.alias(TEST_GENERATOR)
        self.assertIsInstance(test_gen, types.GeneratorType)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], list(test_gen))


class ClassTestCase(BaseJsonTestCase):

    def test_b(self):
        object_b = self.alias(B())
        self.assertIsInstance(type(object_b), type(B))
        self.assertIsInstance(type(object_b), type(A))
        self.assertEqual(B().info(), object_b.info())

    def test_c(self):
        object_c = self.alias(C())
        self.assertIsInstance(type(object_c), type(C))
        self.assertIsInstance(type(object_c), type(B))
        self.assertIsInstance(type(object_c), type(A))
        self.assertEqual(C().info(), object_c.info())

    def test_mro(self):
        self.assertEqual(str(C.__mro__), str(self.alias(C).__mro__))
        self.assertEqual(str(B.__mro__), str(self.alias(B).__mro__))
        self.assertEqual(str(A.__mro__), str(self.alias(A).__mro__))
        self.assertEqual(str(Human.__mro__), str(self.alias(Human).__mro__))

    def test_class_method(self):
        human = self.alias(Human)
        self.assertIsInstance(type(human), type(Human))
        self.assertIsInstance(type(human(20, "Jeka")), type(Human))
        self.assertEqual(str(human.get_const), str(human.get_const))
        self.assertEqual(Human.get_const(), human.get_const())

    def test_static_method(self):
        human = self.alias(Human)
        self.assertEqual(type(Human.static), type(human.static))
        self.assertEqual(Human.static(), human.static())

    def test_property(self):
        human = self.alias(Human)

        human1 = Human(20, "Jeka")
        human2 = human(20, "Jeka")

        self.assertIsInstance(type(human), type(Human))
        self.assertIsInstance(type(human1), type(Human))
        self.assertIsInstance(type(human2), type(Human))

        self.assertEqual(human1.age, human2.age)
        self.assertEqual(human1._name, human2._name)

        human1.age *= 77
        human2.age *= 77
        self.assertEqual(human1.age, human2.age)

        del human2.age
        self.assertEqual('DELETED', human2._name)


if __name__ == '__main__':
    unittest.main()
