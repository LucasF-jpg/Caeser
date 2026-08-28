def caesar_verschluesseln(text, shift):
    ergebnis = ""
    for zeichen in text:
        if zeichen.isalpha():
            basis = ord('A') if zeichen.isupper() else ord('a')
            neu = (ord(zeichen) - basis + shift) % 26
            ergebnis += chr(basis + neu)
        else:
            ergebnis += zeichen
    return ergebnis

def caesar_entschluesseln(text, shift):
    return caesar_verschluesseln(text, -shift)

modus = input("(v)erschlüsseln oder (e)ntschlüsseln? ")
text = input("Text eingeben: ")
shift = int(input("Shift eingeben: "))

if modus == "v":
    print("Verschlüsselt:", caesar_verschluesseln(text, shift))
else:
    print("Entschlüsselt:", caesar_entschluesseln(text, shift))