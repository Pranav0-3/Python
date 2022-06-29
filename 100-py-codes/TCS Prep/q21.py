# Sum of series.

num = 1 
sum = 0.0

while (num<=7):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
        i = i+1

    sum = sum + (num/fact)
    num = num + 1

print("sum of series is: ",round(sum,5))