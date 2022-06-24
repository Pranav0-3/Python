
## Method 1: Using if-else ladder.

month = int(input("Enter the No. of Month: "))
year = int(input("Enter the year: "))

if ((month == 2) and ((year%4==0) or ((year%100==0) and(year%400==0)))):
    print("No of days in month of",month,"are 29")

elif (month == 2):
    print("No of days in month of",month,"are 28")

elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("No of days in month of",month,"are 31")

else:
    print("No of days in month of",month,"are 30")





## Method 2 : Using array

arr = [31,28,31,30,31,30,31,31,30,31,30,31]
month = 8
year = 2003

if (month == 2 and ((year%400==0) or ((year%100!=0) and (year%4==0)))):
    print("no of days is:",arr[month-1]+1)
else:
    print(arr[month-1])
