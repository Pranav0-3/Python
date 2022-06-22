# # Automorphic Number
# # A number whose square ends with the same number is known as an Automorphic number.
# # Let's try and understand it even better using an example ,

# # Example
# # Input : number = 5
# # Output : It's an Automorphic number.
# # Explanation : Number = 5
# # Square of number = 25
# # as the square of the number ends with the number itself, 
# # It's an Automorphic number.



num = int(input("Enter a number:"))
square = pow(num , 2)
mod = pow(10, len(str(num)))

if square%mod == num:
    print("It's a Automorphic number")
else: 
    print("It's not Automorphic")




## Using Endswith() Method
## The endswith() method returns True if the string ends with the specified value, otherwise False.


num1 = int(input("Enter a number: "))
a = str(num1)

num2 = num1**2
b = str(num2)

if b.endswith(a):
    print("AUTOMORPHIC")
else:
    print("NOT AUTOMORPHIC")