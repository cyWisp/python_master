import unittest
from my_sum.my_sum import my_sum


class TestSum(unittest.TestCase):
    def test_list_int(self):

        """
        Test that it can sum a list of integers
        """

        data = [1, 2, 3]
        result = my_sum(data)
        self.assertEqual(result, 6, 'Incorrect sum.')

    def test_tuple_int(self):
        """
        Test that it can sum a tuple of integers
        """

        data = (1, 2, 5)
        result = my_sum(data)
        self.assertEqual(result, 6, 'Incorrect sum.')


if __name__ == '__main__':
    unittest.main()
