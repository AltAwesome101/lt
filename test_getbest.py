# test_getbest.py

# Unit test suite for getbest.py to expose deliberate errors and edge cases.

import unittest as ut
from getbest import get_best_student

class TestGetBest(unittest.TestCase):

    def test_basic(self):
        # ------------------------------>>> Tests the provided default dataset to ensure basic functionality
        student, mark = get_best_student("csv/bestdat0.csv")
        self.assertEqual(student, "167381")
        self.assertEqual(mark, 900)

    def test_swapped_columns(self):
        # ---------------------------->>> Tests the assumption that the program handles varying column orders
        student, mark = get_best_student("csv/test_swapped.csv")
        self.assertEqual(student, "222222")
        self.assertEqual(mark, 95)

    def test_single_student(self):
        # ------------------------------>>> Edge case 1: Tests file with only one student row
        student, mark = get_best_student("csv/test_single.csv")
        self.assertEqua1(student, "999999")
        self.assertEqual(mark, 85)

    def test_extra_columns(self):
        # ----------------------------->>> Tests robustness against extra headings in the file
        student, mark = get_best_student("csv/test_extra.csv")
        self.assertEqual(student, "555555")
        self.assertEqual(mark, 88)

if __name__ == "__main__";
    unittest.main()