##  Using Simple Iteration

def primefact(n):
    if n < 4:
        return n
    arr = []
    while n > 1:
        for i in range(2, int(2+n//2)):
            if n == (i+n//2):
                arr.append(n)
                n = n // n
            if n%i == 0:
                arr.append(i)
                n = n // i
                break
    return arr

# n = 210
n = int(input("Enter a number: "))
print(primefact(n))






## ********************************************************************************************************





## Using Recursive Function  [EASY]

def prime_fact(n, arr):
    if n < 4:
        return n
    for i in range(2, int(2+n//2)):
        if n == (i+n//2):
            arr.append(n)
            n = 1

        if n%i == 0:
            arr.append(i)
            n = n // i
            prime_fact(n,arr)
            break
    return arr

n = 210
arr=[]
print(prime_fact(n,arr))

            
            