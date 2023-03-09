import unittest


def encrypt(clear_text, key):
    return


class Test(unittest.TestCase):
    def test_encrypt_same_length(self):
        self.assertEqual(encrypt("", ""), "")
        self.assertEqual(encrypt("A", [1]), "A")
        self.assertEqual(encrypt("AB", [1, 2]), "AB")
        self.assertEqual(encrypt("AB", [2, 1]), "BA")

    def test_encrypt_longer_key(self):
        self.assertEqual(encrypt("AB", [1, 2, 3]), "AB")
        self.assertEqual(encrypt("AB", [2, 1, 3]), "BA")
        self.assertEqual(encrypt("ABC", [3, 1, 2]), "CAB")

    def test_encrypt_shorter_key(self):
        self.assertEqual(encrypt("ABCD", [1]), "A")
        self.assertEqual(encrypt("ABCD", [1, 2]), "AB")
        self.assertEqual(encrypt("ABCD", [2, 1]), "BA")
        self.assertEqual(encrypt("ABCD", [1, 2, 3]), "ABC")
        self.assertEqual(encrypt("ABCD", [3, 2, 1]), "CBA")
