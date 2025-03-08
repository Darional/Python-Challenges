import unittest
from Challenge1 import string_obtainer 
from Challenge2 import reverse_strings

class TestChallenge1(unittest.TestCase):
    def test_Challenge_1(self):
        self.assertEqual(string_obtainer("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(string_obtainer("3[a2[bc]]"), "abcbcabcbcabcbc")
        self.assertEqual(string_obtainer("a"), "a")
        self.assertEqual(string_obtainer("10[a]"), "aaaaaaaaaa")

    def test_Challenge_2(self):
        self.assertEqual(reverse_strings("Hello"),"olleH")
        self.assertEqual(reverse_strings("Python"),"nohtyP")

if __name__ == '__main__':
    unittest.main()