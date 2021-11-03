# tests for the string_to_lower() function
import unittest


class TestStringToLower(unittest.TestCase):
    def test_string_to_lower(self):
        number = 18
        numbers = [15, 12, 5]
        # testing for an exception one way
        self.assertRaises(ValueError, string_to_lower, number)

        # testing for an exception another way
        with self.assertRaises(ValueError):
            string_to_lower(numbers)


if __name__ == '__main__':
    unittest.main()
