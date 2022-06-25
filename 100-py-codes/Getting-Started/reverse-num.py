
### Method 1 Using Simple Iteration
### Run a while loop with the condition number >0.
### Extract the last digit as Remainder using Modulo operator.
### Using the formula reverse = ( reverse * 10 ) + remainder , we keep changing the reverse value.
### Break down the Nunber using divide operator.
### Print the reverse variable



n = int(input("Enter a number:"))
rev=0

while n>0:
    rev = rev * 10 + n % 10
    n=n//10

print(rev)


## ***********************************************************************************************************



### Method 2: Using String Slicing
##-1 displays index in reverse order, but we should convert it into string

num = int(input("Enter Number:"))
print(str(num)[::-1])                    



## ***********************************************************************************************************




### Method 3: Using Recursion
### Define a recursive function recursum() that takes in number and reverse variable as arguments.
### Set the base case as number == 0 and step recursive call as recursum(num/10, reverse).
### Print the returned value using print() function


def recursum(number,reverse):
  if number==0:
    return reverse
  remainder = int(number%10)
  reverse = (reverse*10)+remainder
  return recursum(int(number/10),reverse)

num = int(input("Enter number to be reversed: "))
reverse = 0
print("The reversed order is: ",recursum(num,reverse))
 