import unittest

from src.StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.stringCalculator = StringCalculator()

    def test_for_empty_string_input(self):
        self.assertEqual(0,self.stringCalculator.add(""))

    def test_for_string_input_with_one_char(self):
        self.assertEqual(1,self.stringCalculator.add("1"))