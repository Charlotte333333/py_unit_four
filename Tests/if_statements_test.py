import unittest
from even_odd import even_or_odd
from abs_value import absolute


class MyTestCase(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual("13 is an odd number", even_or_odd(13))
        self.assertEqual("24 is an even number", even_or_odd(24))

    # In the space below, write a test function for bonus. Make sure to import the appropriate information
    # at the top of this file. Make sure to write three test cases.
    def test_bonus(self):
        # when you are ready to write your tests, go ahead and delete pass
        pass

    def test_absolute(self):
        self.assertEqual(9, absolute(-9))





if __name__ == '__main__':
    unittest.main()
