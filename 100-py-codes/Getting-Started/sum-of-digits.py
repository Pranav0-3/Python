## Method 1:

num = input("Enter numbers:")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)



## ***********************************************************************************************************




## verification for me
## num = 12345
## n = num%10
## print(n) #ans 5



## ***********************************************************************************************************


## Method 2: Using Recursion

num = int(input("Enter numbers:"))
sum = 0

def findSum(num, sum):
    if num == 0:
        return sum

    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)

print(findSum(num, sum))
