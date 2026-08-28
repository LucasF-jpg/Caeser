def crypt(cyph, k):
    res = ""
    for i in cypher:
        i = chr(ord(i) + k)
        if ord(i) > ord("z"):
            i = chr(ord(i) - 26)
        res += i
    print(f"{res}")

cypher = input()
key = 1
while key < 26:
    crypt(cypher, key)
    key += 1



