# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):

    def test_when_output_true(self):
        numbers = [2, 4, 8, 12, 26, 34]

        for n in numbers:
            self.assertTrue(is_even(n))

    def test_when_output_false(self):
        numbers = [5, 7, 9, 15, 35, 57]

        for n in numbers:
            self.assertFalse(is_even(n))


if __name__ == '__main__':
    unittest.main()
