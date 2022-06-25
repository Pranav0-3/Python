## Method 1 : Armstrong for a GIVEN RANGE
## 153 = (1^3 + 5^3 + 3^3) == 153


low = int(input("Enter starting number: "))
high = int(input("Enter ending number: "))

for n in range(low, high + 1):
    order = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        print(n, end=" ")



