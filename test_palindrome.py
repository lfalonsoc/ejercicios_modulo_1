from Python_Programming_Best_Practices import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        test = "reconocer"
        self.assertEqual(is_palindrome(test), True)

if __name__ == '__main__':
    unittest.main()