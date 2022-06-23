## Can A Number Be Expressed As A Sum Of Two Prime Numbers? 


# # Algorithm
# # Take number as input in n
# # Initialize a variable flag as 0
# # Iterate using for loop from value of i between (2, n/2)
# #  For each iteration Call a function sum_of_two_primes for value of i is it returns 1
# # Call same function for value n-i and if it is also 1 then print i and n-i as answer increment the flag to 1
# # If flag is 0 print not possible
# # Create function sum_of_two_prime where check if passed number is prime return true else false

## E.g: N = 30
## OP: 7+23, 13+17, 11+19.


## Correct Method:

num = int(input("Enter a Prime Number:"))
arr = []

for i in range(2,num):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1 
    if flag == 0:
        arr.append(i)

flag = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == num:
            print(str(arr[i])+ " and " +str(arr[j])+ " are the sum of " +str(num))
            break
if flag == 0:
    print("The sum cant be made with prime number:" +str(num))









## EASY WAY: STILL WORKING ON IT :(


# val=int(input("Enter the value:"))
# num=[] 
# for a in range(val):
#     if a > 1:
#         for x in range(2, a):
#             if a % x == 0:
#                 break
#             else: 
#                 num.append(a) 
#                 for x in range(len(num)):
#                     for i in range(len(num)):
#                         if num[x]+num[i]==val:
#                             if num[x]<=num[i]:
#                                 print(num[x], " and ", num[i], " are prime numbers when added gives", val)






