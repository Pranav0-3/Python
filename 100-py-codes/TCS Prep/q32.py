# read an array of input from user and print all odd numbers.


n = int(input("Enter number: "))
l = []

for i in range(n):
    l.append(int(input("Enter here: ")))
    
    list_of_odds = []

    for element in l:
        if element%2 != 0:
            list_of_odds.append(element)

    print(list_of_odds)