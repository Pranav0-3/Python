# print if its available in list or not and mention their type
# Error


lst = []
flag = 0
n = int(input("Enter the no of count: "))

for i in range(0,n):
    ele = input()
    lst.append(ele)

    search_ele = input("Enter what you want to search: ")
    for i in lst:
        if(i == search_ele):
            flag += 1

    if (str(search_ele).isdigit()):
        print(search_ele, "is numeric")
    else:
        print(search_ele, "is string")

    if (flag != 0):
        print("Yes it exists in list.")
    else:
        print("No, it does not exists in list.")
