clear_msg = input("Welche Nachricht soll verschlüsselt werden?")


#clear_msg = ""
clear_msg = clear_msg.lower()
cypher_msg = ""
for char in clear_msg:
    if char == " ":
        cypher_msg += "-"
    elif char == ".":
        cypher_msg += "_"
    elif char == "?":
        cypher_msg += "Y"
    elif char == "!":
        cypher_msg += "X"

    else:
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
print(cypher_msg)
