marks = int(input("Enter marks:"))
year = int(input("Enter year:"))
age = int(input("Enter age:"))

if marks > 80 and year < 2020 and age > 18:
    print("{}:true".format(age))
else:
    print("{}:false".format(age))