def caesar_verschluesseln(text, shift):
    ergebnis = ""
    for zeichen in text:
        if zeichen.isalpha():
            basis = ord('A') if zeichen.isupper() else ord('a')
            neu = (ord(zeichen) - basis + shift) % 26
            ergebnis += chr(basis + neu)
        else:
            ergebnis += zeichen  # Leerzeichen & Satzzeichen bleiben unverändert
    return ergebnis

text = input("Text eingeben: ")
shift = int(input("Shift eingeben: "))
print("Verschlüsselt:", caesar_verschluesseln(text, shift))