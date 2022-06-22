# ==== Convert binary to decimal in Python ======

a = (input("Enter binary: "))           # input a binary
b = int(a,2)                            # base 2 to base 10
print(b)                                # 204, <class 'int'>







# Binary to Decimal

num = int(input("Enter a binary number:"))
binary = num
decimal_val = 0
base = 1

while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary number {}\nDecimal Number {}".format(binary, decimal_val))

