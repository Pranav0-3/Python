
# Easy Way:

num = int(input("Enter a decimal number: "))
binary = bin(num)
print(binary)




# Algorithm


def dectobin(num):
    binaryArray = []
    while num > 0:
        binaryArray.append(num % 2)
        num = num // 2
    for j in binaryArray:
        print(j, end="")

dec = int(input("Enter Deci Number: "))
print(dectobin(dec))