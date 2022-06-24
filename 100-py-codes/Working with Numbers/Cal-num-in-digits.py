def count(n):
    digit = 0
    
    while n!= 0:
        n //= 10
        digit += 1
    return digit

n = int(input("Enter the number: "))
print("No. of digits are: %d" % count(n))





# Another Method

import math
n = 3258
digit = math.floor(math.log10(n)+1)
print("The Total digits are:", digit)