import unittest
from Challenge1 import string_obtainer 

class TestChallenge1(unittest.TestCase):
    def test_Challenge_1(self):
        self.assertEqual(string_obtainer("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(string_obtainer("3[a2[bc]]"), "abcbcabcbcabcbc")
        self.assertEqual(string_obtainer("a"), "a")
        self.assertEqual(string_obtainer("10[a]"), "aaaaaaaaaa")

if __name__ == '__main__':
    unittest.main()