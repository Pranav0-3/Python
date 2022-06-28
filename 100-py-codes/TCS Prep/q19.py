# MIN MAX and SUM of digit


num = int(input("Enter a number:"))
large = 0
small = 9
count = 0

while num > 0:
    rem = num%10
    count = count+rem
    if large<rem:
        large = rem
    elif small>rem:
        small = rem
    num //= 10

print("largest digit is {}".format(large))
print("Smallest digit is {}".format(small))
print("sum of digit is {}".format(count))