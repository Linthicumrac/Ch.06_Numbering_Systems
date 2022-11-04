print(chr(33))
word = input("enter a word to encrypt")
encrypted = " "
normLetter = " "
for letter in word:
    i = ord(letter)+5  # +5 shift ( a = e, b = f, etc) (kinda like a ce asar shift)
    newLetter = chr(i)  # back to a letter
    encrypted += newLetter
print(encrypted)

