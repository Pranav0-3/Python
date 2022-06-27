# Write a py pgm to read a string from the console and print each character of the 
# string on a seperate line.


str = input("Enter a string: ")
for i in range(len(str)):
    print(str[i])