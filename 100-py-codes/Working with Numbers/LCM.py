##

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
for i in range(max(num1,num2), 1+(num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is", lcm)







## LCM formula: num1*num2//HCF

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

for i in range(1, max(num1,num2)):
    if num1 % i == num2 % i == 0:
        HCF = i

LCM = (num1*num2)//HCF
print(LCM)









# Recursion

def HCF(a,b):
    return b == 0 and a or HCF(b, a%b)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

hcf = HCF(num1,num2)
lcm = (num1*num2)//hcf
print(lcm)