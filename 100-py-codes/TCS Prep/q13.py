# read date as ddmmyyyy and displaying day,month,year

date = input("Enter a date in ddmmyyyy format: ")

print("Day:"+date[:2])
print("Month:"+date[2:4])
print("Year:"+date[4:])