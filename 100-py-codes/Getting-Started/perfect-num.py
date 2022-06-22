
# # Perfect Number
# # A Number that can be represented as the sum of all the factors of the number 
# # is known as a Perfect Number

# # Example
# # Input : 28
# # Divisors : [1, 2, 4, 7, 14]
# # Sum = 1 + 2 + 4 + 7 + 14 = 28
# # Output : It's a Perfect Number

## Method: For Loop Iteration between [1, num]

num = int(input("Enter a number:"))
sum = 0

for i in range(1,num):
    if num%i == 0:
        sum += i 
    
if sum == num:
    print(num,"is a perfect number")
else:
    print(num,"is not perfect number")





## *********************************************************************************************************




## Method 2: While loop 

num = int(input("Enter a number:"))
# num = 28
sum = 0

i = 1
while i < num:
    if num % i == 0:
        sum += i

    i += 1
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")




## *********************************************************************************************************





## Method 3: Iteration between [1, num/2+1]


num = 28
sum = 0

for i in range(1 , num//2+1):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect NUmber")