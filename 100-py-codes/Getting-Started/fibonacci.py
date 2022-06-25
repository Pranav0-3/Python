# It’s a unique sequence where the next number is the sum of previous two numbers.
# Where the first two terms are always 0 and 1

# Method 1

num = int(input("Enter number of series you want: "))
num1 = 0
num2 = 1

print("FIBONACCI SERIES: ", num1, num2, end=" ")
for i in range(2, num):
    num3 = num1+num2
    num1 = num2
    num2 = num3
    print(num3, end=" ")

print()





## ***********************************************************************************************************



## Yield Method:   

def cal(limit):
    a,b = 0,1
    while a < limit:
        yield a 
        a,b = b,a+b

limit = int(input("Enter the limit: "))
fibonacci = cal(limit)
for i in fibonacci:
    print(i, end=" ")

