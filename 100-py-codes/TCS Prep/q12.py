# fibonacci series

num = int(input("Enter number of series you want: "))
num1 = 0
num2 = 1

print("Fibonacci Series:", num1, num2, end=' ')
for i in range(2, num):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3, end=" ")
print()





# ************************************************************************************




def fib(n):
    a = 0
    b = 1
    if (n >= 0):
        print(a, end=' ')
    if (n >= 1):
        print(b, end=' ')
    for i in range(2, n+1):
        print(a + b, end=' ')
        b = a + b
        a = b - a 
num = int(input("Enter a number: "))
print(fib(num))