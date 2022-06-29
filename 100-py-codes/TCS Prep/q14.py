# read a string from console and print the count of vowels.

words = input("Enter a string:")
count = 0

for i in words:
    if i.lower() in ["a","e","i","o","u"]:
        count += 1

print(count)





#************************************************************************


# read the string from input and print the count of each vowels.


w = input("Enter a string: ")
for char in ["a","e","i","o","u"]:
    c = 0

    for letter in w:
        if letter.lower() == char:
            c += 1
    print("{} - {} ".format(char,c))