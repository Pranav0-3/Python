a = int(input("Enter a value: "))
b = int(input("Enter a value: "))

print("\n1.Addition\n2.Subtraction\n3.Exponent\n4.Multiplication")

choice = int(input("\nEnter a choice: "))
if choice == 1:
    print("{} + {} = {}".format(a,b,a+b))
if choice == 2:
    print("{} - {} = {}".format(a,b,a-b))
if choice == 3:
    print("{} ** {} = {}".format(a,b,a**b))
if choice == 4:
    print("{} * {} = {}".format(a,b,a*b))