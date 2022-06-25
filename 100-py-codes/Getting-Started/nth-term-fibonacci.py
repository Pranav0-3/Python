# 0 1 1 2 3 5 8 13 21 34

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number:"))
print(fib(n-1))