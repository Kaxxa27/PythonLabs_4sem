import unittest

from Toolkit.regexservice import text_analysis_with_regex
from Toolkit.stringgluer import text_gluer_with_constants
from constants import CONSTANTS_FOR_SWITCHING, CONSTANTS_FOR_CONTINUE
from Toolkit.analizator import (
    amount_of_sentences,
    amount_of_non_decl_sentences,
    average_word_and_sent_length
)


def text_to_list(text):
    regex = r"\S[^.?!]+[.!?]*"
    return text_gluer_with_constants(text_analysis_with_regex(regex, text),
                                     CONSTANTS_FOR_SWITCHING,
                                     CONSTANTS_FOR_CONTINUE)


class TestAnalizator(unittest.TestCase):

    def test_amount_of_sentences(self):
        self.assertEqual(amount_of_sentences(text_to_list("That's. Is? Text!!!")), 3)
        self.assertEqual(amount_of_sentences(text_to_list("Hello, World...")), 1)
        self.assertEqual(amount_of_sentences(text_to_list("")), 0)
        self.assertEqual(amount_of_sentences(text_to_list("Hi Mr. Eugene. How are you?")), 2)

    def test_amount_of_non_decl_sentences(self):
        self.assertEqual(amount_of_non_decl_sentences(text_to_list("That's. Is? Text!!!")), 2)
        self.assertEqual(amount_of_non_decl_sentences(text_to_list("Hello, World...")), 0)
        self.assertEqual(amount_of_non_decl_sentences(text_to_list("Hi? Jeka?! What you want, Mr. Bro???")), 3)
        self.assertEqual(amount_of_non_decl_sentences(text_to_list("Hi Jn. Eugene. How are you?")), 1)

    def test_average_word_and_sent_length(self):
        self.assertEqual(average_word_and_sent_length(text_to_list("Test.")), (4, 4))
        self.assertEqual(average_word_and_sent_length(text_to_list("Hel lo. Hi. Jek. Py.")), (2.4, 3))
        self.assertEqual(average_word_and_sent_length(text_to_list("hi123j kak. tak 12345 777 888 ")), (4, 6))
        self.assertEqual(average_word_and_sent_length(text_to_list("375! 29! Privet...")), (6, 2))


if __name__ == "__main__":
    unittest.main()
