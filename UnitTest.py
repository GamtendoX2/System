import unittest

def encrypt(clear_msg):
    #clear_msg = ""
    clear_msg = clear_msg.lower()
    cypher_msg = ""
    wasNumber = False
    for char in clear_msg:
        if char == " ":
            cypher_msg += "-"
        elif char == ".":
            cypher_msg += "_"
        elif char == "?":
            cypher_msg += "Y"
        elif char == "!":
            cypher_msg += "X"
        elif char.isdecimal():
            nb = int(char)
            if wasNumber == False:
                cypher_msg += "Z"
            wasNumber = True
            while nb > 0:
                if nb > 7:
                    cypher_msg += "/"
                    nb -= 8
                elif nb > 3:
                    cypher_msg += "|"
                    nb -= 4
                elif nb > 1:
                    cypher_msg += ":"
                    nb -= 2
                elif nb > 0:
                    cypher_msg += "°"
                    nb -= 1
            cypher_msg += "."

        else:
            if wasNumber == True:
                cypher_msg += "Z"
            wasNumber = False
            nb = (ord(char) -96)
            while nb > 0:
                if nb > 7:
                    cypher_msg += "/"
                    nb -= 8
                elif nb > 3:
                    cypher_msg += "|"
                    nb -= 4
                elif nb > 1:
                    cypher_msg += ":"
                    nb -= 2
                elif nb > 0:
                    cypher_msg += "°"
                    nb -= 1
            cypher_msg += "."
    if wasNumber == True:
        cypher_msg += "Z"
    return cypher_msg


class EncryptTest(unittest.TestCase):
    def test_encrypt_lower_single_letter_success(self):
        assert encrypt(clear_msg="a") == "°."
        assert  encrypt(clear_msg="b") == ":."

    def test_encrypt_upper_single_letter_success(self):
        assert encrypt(clear_msg="A") == "°."
        assert  encrypt(clear_msg="B") == ":."

    def test_encrypt_numbers_success(self):
        assert encrypt(clear_msg="1") == "Z°.Z"
        assert  encrypt(clear_msg="12") == "Z°.:.Z"

    def test_encrypt_all_success(self):
        assert encrypt(clear_msg="A1b2.") == "°.Z°.Z:.Z:.Z_"
