# total number of vowels 

word = input("Enter a word: ")
count = 0

for i in word:
    if i.lower() in ["a","e","i","o","u"]:
        count += 1

print(count)





#######


word = input("Ente a word: ")
for char in ["a","e","i","o","u"]:
    c = 0

    for i in word:
        if i.lower() == char:
            c += 1
    print("{}-{}".format(char,c))
