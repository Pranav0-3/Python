num1 = float(input("Enter first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))
if op == "+":
    print("Result is: ",num1+num2)

elif op == "-":
    print("Result is: ",num1-num2)

elif op == "*":
    print("Result is: ",num1*num2)

elif op == "/":
    print("Result is: ",num1/num2)

else:
    print("Error")
