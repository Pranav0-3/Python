## Easy with logic

num1 = int(input("Enter a number:"))
num2 = int(input("Enter power for number: "))
num = num1**num2                          #formula
print("The power of ", num1 ,"is: ",num)



## Method 1: Using pow() Function

num = int(input("Enter a number:"))
power = int(input("Enter the power:"))
print(pow(num,power))





## ***********************************************************************************************************




## Method 2: Using Simple Iteration

num = int(input("Enter a number:"))
power = int(input("Enter the power:"))
output = 1

for i in range(power):
    output*=num

print(output)




## ***********************************************************************************************************




## Method 4: Using Recursion
 
num = int(input("Enter a number:"))
power = int(input("Enter the power:"))
def recurpow(num,power):
    if power == 0:
        return 1
    return num * recurpow(num, power-1)
print(recurpow(num,power))