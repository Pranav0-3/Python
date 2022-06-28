# Armstrong number


int = int(input("Enter a number:"))
temp = int
sum = 0

while temp > 0:
    digit = temp%10
    sum += pow(digit, 3)
    temp //= 10


if int == sum:
    print("{} is a armstrong number".format(int))
else:
    print("{} is not a armstrong number".format(int))