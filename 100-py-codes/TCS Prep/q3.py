# Write a py pgm to read a float value as an input and round it to two decimal digits.


f = float(input("Enter a floating number: "))
float_num = "{:.2f}".format(f)

print(float_num)