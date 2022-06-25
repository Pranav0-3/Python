# Check Whether a Given Number is an Armstrong Number or Not
# Given an integer input, the objective is to check whether or not the given input variable is an Armstrong number.
# In order to do so,
# we check whether
# the sum of the digits of each number to the power the length of the number
# is equal to the number itself or not.
# If the number is the same as the original, it’s an Armstrong number
# 371 can also be represented as 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371 therefore it's an Armstrong Number.


# Method 1: Easy one

num = int(input("Enter a number: "))
number = str(num)
length = len(number)
sum = 0
for i in range(length):
    sum += int(number[i]) ** len(number)

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")




# ************************************************************************************************************




# Method 2 Recusrion :`(
num = int(input("Enter number:"))
number = num
length = len(str(number))
sum = 0

def checkArmstrong(number, length, sum):
    if number == 0:
        return sum

    # single digit(first number) to the pow of length.(repeats for n times)
    sum += pow(int(number % 10), length)
    return checkArmstrong(number/10, length, sum)

if checkArmstrong(number, length, sum) == num:
    print(num, ": is a Armstrong Number")
else:
    print(num, ": is NOT an Armstrong Number")




# # ************************************************************************************************************




