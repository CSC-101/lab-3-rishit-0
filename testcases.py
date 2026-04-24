import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 6
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

# test_double_one giving the right answer doesn't imply that the double function is correct.
# For the value of 2, 2*2=2**2, so it outputs the expected value even if the code is fundamentally incorrect.
