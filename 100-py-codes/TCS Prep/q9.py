# print true if it's palindrome or else print false

def ispalindrome(n):
    return n == n[::-1]

n = (input("Enter a num to check palindrome: "))
ans = ispalindrome(n)

if ans:
    print("True")
else:
    print("No")
