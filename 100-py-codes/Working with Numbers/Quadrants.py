x = int(input("Enter x co-ordinate: "))
y = int(input("Enter y co-ordinate: "))

if x > 0 and y > 0:
    print("It's a first Quad")
elif x < 0 and y > 0:
    print("It's a second Quad")
elif x < 0 and y < 0:
    print("It's a third Quad")
elif x > 0 and y < 0:
    print("It's a fourth Quad")

elif x == 0 and y == 0:
    print("It's orgin")
elif x != 0 and y == 0:
    print("X-axis")
elif x == 0 and y != 0:
    print("Y-axis")