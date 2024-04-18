# https://realpython.com/python-testing/#more-advanced-testing-scenarios
import unittest
from sum_thing import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2]
        result = sum(data)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()