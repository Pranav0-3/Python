## Select whole file with crtl+a and press "ctrl+/" to uncomment.

## Method 1: Using Brute Force


num = int(input("Enter Number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("ZERO")








## Method 2: Using Nested if-else Statements

num = int(input("Enter any Number: "))
if num >= 0:
    if num == 0:
        print("ZERO")
    else:
        print("Positive Number")
else:
    print("Negative Number")








## Method 3: Using Ternary Operator

## Ternary Operator Syntax:
## ( Condition ) ? ( if True : Action) : ( if False : Action) ;

num = int(input("Enter any Number: "))
print("Postive" if num > 0 else "Negative")