import unittest
import os
try:
    from Challenge1 import string_obtainer 
    from Challenge2 import reverse_strings
except ImportError:
    print("Warning: There is a/some files or functions that aren't created ")

class TestChallenge1(unittest.TestCase):
    @unittest.skipIf(not os.path.exists("Challenge1.py"), "Skipping Challenge1, it doesn't exists")
    def test_Challenge_1(self):
        self.assertEqual(string_obtainer("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(string_obtainer("3[a2[bc]]"), "abcbcabcbcabcbc")
        self.assertEqual(string_obtainer("a"), "a")
        self.assertEqual(string_obtainer("10[a]"), "aaaaaaaaaa")
        print("Challenge 1: Ok")

    @unittest.skipIf(not os.path.exists("Challenge2.py"), print("Skipping Challenge2, it doesn't exist"))
    def test_Challenge_2(self):
        self.assertEqual(reverse_strings("Hello"),"olleH")
        self.assertEqual(reverse_strings("Python"),"nohtyP")
        print("Challenge 2: Ok")

if __name__ == '__main__':
    unittest.main()