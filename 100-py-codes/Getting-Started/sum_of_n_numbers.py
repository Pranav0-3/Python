##method1
num = int(input("Enter Number:"))
sum = 0                             #Initialize a variable sum = 0.
for i in range(num+1):              #Using a for loop in iteration ‘i’ iterate between [1, num].
    sum+=i                          #Each time add ‘i’ to current sum as sum = sum + i.
print(sum)


## ***********************************************************************************************************




## Method 2

num = int(input("Enter Number:"))
print(num*(num+1)/2)



## ***********************************************************************************************************



##Method 3

def getsum(num):
    if num == 1:
        return 1
    return num + getsum(num-1)

num = int(input("Enter a number: "))
print(getsum(num))


## Initialize a variable sum = 0.
## Call function getSum (num).
## In each recursive call add the current value of n and call for lower recursion call using return num + getSum(num-1);
## Print sum value



