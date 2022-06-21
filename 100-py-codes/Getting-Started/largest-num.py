## MEthod 1 Using if-else Statements 2 digits

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
if n1>n2:
    print("The largest number is: ", n1)
else:
    print("The largest number is: ", n2)


## ***********************************************************************************************************




## Method 2  Using Ternary Operator

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(num1 if num1>num2 else num2)


## ***********************************************************************************************************




## Method 3: Using inbuilt max() Function
no1 = int(input("Enter a number: "))
no2 = int(input("Enter another number: "))
print(max(no1,no2))



## ***********************************************************************************************************




## 3 Digit Greatest numbe
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if n1>=n2 and n1>=n3:
    print("The largest no is: ", n1)
elif n2>=n2 and n2>=n3:
    print("The largest no is: ", n2)
else:
    print("The largest no is: ", n3)



## ***********************************************************************************************************





## Method : Using Nested if-else Statements

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1>=n2:
    if n1>=n3:
        print(n1)
elif n2>=n1:
    if n2>=n3:
        print(n2)
else:
    print(n3)