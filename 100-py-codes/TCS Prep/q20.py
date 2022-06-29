# Min max and Avg with using array to store numbers.

num = int(input("Enter a count: "))
count = 0 
total = 0.0
min = 0
max = 0

print("Enter number: ")
for i in range(num):
    n = int(input())
    count = count +1
    total = total+n

    if (i==0):
        min = n
    if n<min:
        min = n
    elif n>max:
        max = n

print("AVG is:", total/num)
print("Minimum is: ",min)
print("Maximum is ",max)