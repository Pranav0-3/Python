# Method 1: Simple iterative solution
# If the number is greater than 2.
# If the number has any factors in the range [2,number].
# If any off the above conditions are satisfied, the number isn’t a Prime.


num = int(input("Enter a number:"))
flag = False

for i in range(2, num+1):
    if num % i == 0:
        flag = True
        break

if flag == True:
    print("Not Prime")
else:
    print("Prime")



## ***********************************************************************************************************





## Method: Basic Recursion technique
## Declare a recursive function checkPrime() with base cases as follows
## if number == iter, return True.
## if number < 2, return False.
## if number % iter == 0, return False.
## Set the Recursive step call as checkPrime(number,iter+1).


num = int(input("Enter a number:"))
def checkPrime(num, iter=2):
    if num == iter:
        return True
    if num < 2:
        return False
    if num % iter == 0:
        return False
    return checkPrime(num,iter+1)
if checkPrime(num) == True:
    print("Prime")
else:
    print("Not Prime")


