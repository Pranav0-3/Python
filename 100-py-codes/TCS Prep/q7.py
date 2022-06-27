# marks and grade qus.


marks = int(input("Enter the marks: "))

if marks >= 80:
    print("{} will grant you Grade A".format(marks))
elif marks >= 60:
    print("{} will grant you Grade B".format(marks))
else:
    print("{} will grant you Grade C".format(marks))