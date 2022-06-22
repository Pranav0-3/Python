
# Example
# Input : 10
# Output : 2 5


def factor(n):
    i = 1
    while i<= n:
        if(n % i == 0):
            print(i, end=" ")
        i = i+1
        
n = int(input("Enter the number:"))
print("The factors are:")
factor(n)






















def factor(n):
    i = 1
    while i<=n:
        if n%i == 0:
            print(i,end=' ')
        i = i+1

n = int(input("Enter user input: "))
print("The factors are: ")
factor(n)