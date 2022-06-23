## Easy Way:

num = int(input("Enter deci number: "))
octal = oct(num)
print("The octal number is: ", octal)





## Algorithm

DectoOct= int(input("Enter a number: "))
octal = []
while DectoOct > 0:
    r = DectoOct % 8
    octal.append(r)
    DectoOct = DectoOct // 8
for i in reversed(octal):
    print(i, end="")









