# read a num and print if prime or not

num = int(input("Enter a number: "))
def checkprime(num , iter=2):
    if num == iter:
        return True
    if num < 2:
        return False
    if num%iter == 0:
        return False
    return checkprime(num , iter+1)

if checkprime(num) == True:
    print("PRIME")
else:
    print("NOT PRIME")
