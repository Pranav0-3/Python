
## Replace all the 0s with 1s
## eg: 14005400 should be displayed as: 14115411


# Algorithm
# Take Input in num and initialize a variable num with with value 0
# If num is equals to zero then update the value of num2 to 1
# Iterate using a while loop until num is greater then 0
# For each iteration initialize a variable rem and store unit digit of num
# If rem equals to 0 then set rem to 1
# Set num to num divide by 10 & num2 equals to num2*10+rem
# Reverse and print num2


## Easy Way:

from dataclasses import replace

num = int(input("Enter a number containing Zero:"))
num = str(num)
convert = num.replace("0", "1")
print("Converted number to:", convert)