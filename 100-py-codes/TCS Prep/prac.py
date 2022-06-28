c = input("Enter a charector : ")


def lower(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


def capital(c):
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


if not c.isalpha():
    print("Non alphabet")
elif lower(c) or capital(c):
    print(c, "is a Vowel")
else:
    print(c, "is a consonant")