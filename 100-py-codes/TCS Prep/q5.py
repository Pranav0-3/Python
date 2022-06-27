# Even natural and odd natural && even and odd numbers.


num = int(input("Enter a number: "))

if num > 0 and num%2==0:
    print("{} is an Even natural number".format(num))
if num > 0 and num %2 != 0:
    print("{} is an Odd natural number".format(num))


if num == 0 and num%2==0:
    print("{} is an Even number".format(num))
if num < 0 and num %2 != 0:
    print("{} is an Odd number".format(num))

