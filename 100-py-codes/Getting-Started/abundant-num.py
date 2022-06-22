## Method 1: Using Range until Number

# num = 12
num = int(input("Enter a number to check:"))
sum = 1

for i in range(2,num):
    if num % i == 0:
        sum = sum + i

if (sum>num):
    print("It's an Abundant Number")
else:
    print("It's not an Abundant Number")


