## Reverse a number


# EASY:

num = input("Enter a value: ")
print(num[::-1])



# *************************************************************************




## Logical method :(

num = int(input("Entere a number: "))
revs = 0

while num != 0:
    digit = num%10
    revs = revs * 10 + digit 
    num //= 10

print(revs)