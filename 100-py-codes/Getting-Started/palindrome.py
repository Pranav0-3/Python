## For a number to be a Palindrome, the number must be the same when reversed. 
## If the number doesn’t match the reverse of itself, the number is not a Palindrome


## 1 Simple method

num = list(input("Enter numbers to check whether palindrome or not: "))
for i in range(len(num)):
    if num[i] == num[len(num)-1-i]:
        continue
    else:
        print("Not Palindrome")
        break
else: 
    print("Palindrome")


## ***********************************************************************************************************




## Method 2

num = int(input("Enter some digits:"))
temp = num
rever = 0

while temp > 0:
    rem = temp % 10
    rever = (rever * 10) + rem
    temp = temp // 10

if num == rever:
    print("Palindrome")
else:
    print("Not Palindrome")





## ***********************************************************************************************************



## Method 3: Using slicing

num = int(input("Enter some digits:"))
reverse = int(str(num)[::-1])

if num == reverse:
    print("Palindrome")
else: 
    print("Not Palindrome")



## ***********************************************************************************************************



## Method 4: Recursion
def recurpalin(num, rev):
    if num == 0:
        return rev

    rem = int(num % 10)
    rev = (rev*10) + rem
    return recurpalin(int(num / 10), rev)

num = int(input("Enter few digits:"))
rev = 0
rev = recurpalin(num, rev)

# print(str(num) + ' is: ', end="") #optional: string conversion
print("palindrome" if rev == num else "not palindrome")




## ***********************************************************************************************************




## Method 5: Using In-Built reversed function for string
 
def checkpalindrome(str):
    reverse = ''.join(reversed(str))

    if str == reverse:
        return True
    return False 


s = str(input())

if checkpalindrome(s):
    print("Palindrome") 
else:
    print("Not a palindrome")