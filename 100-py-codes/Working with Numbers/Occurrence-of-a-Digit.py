
# Method 1 : Algorithm

def countdigit(n,d):
    count = 0

    while (n > 0):
        if (n % 10 == d):
            count += 1
        n //= 10
    return count

n = int(input("Enter a number: "))
d = int(input("Enter the num you want to count occurance of: "))

print("The number", d ,"occured",countdigit(n,d), "times")






## Method 2: Using count function

num = 28352828
digit = 2

str1 = str(num)
str2 = str(digit)

print(str1.count(str2))