# Write a pgm to read 4 dgit int value as a input and perform sum of all digits of input int.

num = input("Enter 4 digit num: ")
sum = 0

for i in num:
    if len(num) < 5:
        sum = sum + int(i)

print(sum)