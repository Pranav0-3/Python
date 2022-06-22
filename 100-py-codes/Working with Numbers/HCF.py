## Linear Quest

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
hcf = 1

for i in range(1, min(num1,num2)):
    if num1%i == 0 and num2%i == 0:
        hcf = i
print("HCF of", num1, "and", num2 , "is", hcf)





## Repeated Subtraction with Modulo Operator using Recursion Algorithm


def HCF(a,b):
    return b == 0 and a or HCF(b, a%b)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
# num1 = 36
# num2 = 60
print("hcf of", num1, "and", num2, "is", HCF(num1,num2))