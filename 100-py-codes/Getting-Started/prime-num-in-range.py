n1 = int(input("Enter the starting number:"))
n2 = int(input("Enter the ending number: "))
primes = []

for i in range(n1, n2+1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue
    

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
print(primes)







# EASY:

n1 = int(input("Enter the starting number:"))
n2 = int(input("Enter the ending number: "))
for n in range(n1, n2+1):
    if n > 1:
        for i in range(2,n):
            if n%i == 0:
                break
        else:
            print(n, end=" ")
