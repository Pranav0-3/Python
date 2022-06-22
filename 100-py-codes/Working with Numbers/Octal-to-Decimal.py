# Easy Way:

oct_num = int(input("Enter octal number: "))
decimal_val = int(str(oct_num), 8)
print("Oct value {}\nDecimal Value {}".format(oct_num, decimal_val))





# Algorithmic way

def OctDec(num):
    deci = 0
    base = 1

    while num:
        last_digit = num % 10                 #512 % 10 = 2
        num = int(num / 10)                   #512 / 10 = 51.2 so "51"
        deci = deci + last_digit * base         
        base = base * 8
    return deci

octal = int(input("Enter a number: " ))
print(OctDec(octal))
