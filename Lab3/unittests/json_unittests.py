import unittest
from json_serializer.json_serializer import JSON_Serializer
from unittests.code_for_tests import (
    TEST_INT, TEST_FLOAT, TEST_STR,
    TEST_BOOL, TEST_SET, TEST_DICT,
    TEST_LIST, TEST_NONE, TEST_BYTES,
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


if __name__ == '__main__':
    unittest.main()
