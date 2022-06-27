## String Palindrom 
## wasitacaroracatisaw


def isplaindrome(str):
    return str ==str[::-1]
    
str = input("Enter a string: ")
ans = isplaindrome(str)

if ans:
    print("YES")
else:
    print("NO")
