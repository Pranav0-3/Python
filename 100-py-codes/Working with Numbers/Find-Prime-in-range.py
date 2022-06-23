
# EASY WAY:

Lower_Range  =  int(input("Enter the Lower range:"))
Higher_Range =  int(input("Enter the Higher range:"))
for n in range(Lower_Range,Higher_Range+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n,end=" ")







# METHOD 2
from cmath import sqrt
n1 = int(input("Enter the starting number: "))
n2 = int(input("Enter the ending number: "))
primes = []

for i in range(n1 , n2+1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2,i):
        if i % x == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(i)
print(primes)








## Fast execution Method:

from math import sqrt
def checkprime(n):

# 1 AND NEGATIVE NUMBERS ARE NEVER PRIME HENCE RETURN 0(FALSE)
    if n <=1:               
        return 0
    
# 2 IS THE PRIME NUMBER HENCE RETURN 1(TRUE)
    elif n == 2:
        return 1

# IF IT'S MULTIPLE OF 2 THEN ITS NOT PRIME, HENCE RETURN 0(FALSE)
    elif n % 2 == 0:
        return 0

# CHECK FOR ODD NUMBERS NOW
# Return TRUE if "for cond" satisfy with if cond or else return FALSE
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return 0
    return 1                       

a = int(input("Enter the starting point: "))
b = int(input("Enter the ending point: "))
for i in range(a, b+1):
    if checkprime(i):
        print(i, end=" ")
