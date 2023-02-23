cypher_msg = ""







nb = 19
while nb > 0:
    if nb > 7:
        print("/")
        nb -= 8
    elif nb > 3:
        print("|")
        nb -= 4
    elif nb > 1:
        print(":")
        nb -= 2
    elif nb > 0:
        print("°")
        nb -= 1
print(".")
