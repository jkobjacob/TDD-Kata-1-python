import unittest

from src.StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.stringCalculator = StringCalculator()

    def test_for_empty_string_input(self):
        self.assertEqual(0,self.stringCalculator.add(""))

    def test_for_string_input_with_one_char(self):
        self.assertEqual(1,self.stringCalculator.add("1"))

    def test_for_string_input_with_more_than_one_chars(self):
        self.assertEqual(6,self.stringCalculator.add("1,2,3"))

    def test_for_string_input_delimited_by_new_lines(self):
        self.assertEqual(6,self.stringCalculator.add("1\n2,3"))

    def test_for_string_input_with_different_delimiters(self):
        self.assertEqual(3,self.stringCalculator.add("//;\n1;2"))

    def test_for_string_input_with_a_negative_number(self):
        try:
            self.stringCalculator.add("-1,2")
        except ValueError as ve:
            self.assertEqual("negatives not allowed -1", ve.args[0])
        
    def test_for_string_input_with_multiple_negatives(self):
        try:
            self.stringCalculator.add("-1,2,-3")
        except ValueError as ve:
            self.assertEqual("negatives not allowed -1 -3", ve.args[0])

    def test_for_how_many_times_add_was_invoked(self):
        tmp = StringCalculator()
        for _ in range(10):
            _ = tmp.add("")
        
        self.assertEqual(10,tmp.get_called_count())

    def test_whether_numbers_greater_than_1000_are_ignored(self):
        self.assertEqual(2,self.stringCalculator.add("2,1001"))

    def test_for_delimiters_of_any_length(self):
        self.assertEqual(6,self.stringCalculator.add("//[***]\n1***2***3"))