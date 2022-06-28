# print the sum of odd and even digits separately.

num = int(input("Enter a value: "))
sum_odd = 0
sum_even = 0

while num > 0:
    rem = num%10
    if rem%2 == 0:
        sum_even += rem
    else:
        sum_odd += rem
    num //= 10

print("Sum of even digit is {}".format(sum_even))
print("Sum of odd digit is {}".format(sum_odd))