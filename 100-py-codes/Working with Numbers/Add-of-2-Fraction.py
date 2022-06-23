## Python Program for Addition of two fractions

# Algorithm:

# Initialize variables of numerator and denominator
# Take user input of two fraction
# Find numerator using this condition (n1*d2) +(d1*n2 ) where n1,n2 are numerator and d1 and d2 are denominator
# Find denominator using this condition (d1*d2) for lcm
# Calculate GCD of a this new numerator and denominator
# Display a two value of this condition x / gcd, y / gcd


# EASY WAY:

n1 = int(input("Enter 1st Numerator:"))
d1 = int(input("Enter 1st denominator:"))

n2 = int(input("Enter 2nd Numerator:"))
d2 = int(input("Enter 2nd denominator:"))

num1 = (n1*d2)
num2 = (d1*n2)
den = (d1*d2)

res = num1 + num2
print(res, "/", den)