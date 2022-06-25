## method1
num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
sum = 0                             
for i in range(num1, num2+1):              
    sum+=i                          
print(sum)



## ***********************************************************************************************************




## Method 2

num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))

sum = print( (num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)



## ***********************************************************************************************************




# Method recursion

def recursum(sum, n1, n2):
    if n1>n2:
        return sum
    return n1 + recursum(sum,n1+1,n2)

n1 = int(input("Enter num:"))
n2 = int(input("Enter num:"))
sum = 0
print(recursum(sum,n1,n2))
