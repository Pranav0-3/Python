# # Python Program for Permutations In Which N People Can Occupy R Seats In A Classroom

# # Which n people can occupy r seats in a classroom in Python
# # Here, we will discuss program for Permutations In Which N People Can Occupy R Seats in python .
# # In this python program, we will be defining the number of ways in which,
# # N number of students can occupy R number of seats. 
# # Take an example Ten friends enter the classroom late,
# # and all the seats are occupied by toppers of the college, 
# # and now only Six seats are available, 
# # so in how many ways are those Ten friends will occupy Six seats although 4 students have to leave the classroom. 
# # We will use math library for factorial function in building of this program.

# # The formula for a permutation is: P(n,r) = n! / (n-r)!




## Easy Way: Using "math.perm" inbuild function

import math

N = int(input("Enter the number of people: "))
R = int(input("Enter the number of seats: "))
P = math.perm(N,R)
print("The Possible Arrangements are:", P)





## Permutations in which n people can occupy r seats using function definition and formula

def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact = fact * i
    return fact


N = int(input("Enter the number of people: "))
R = int(input("Enter the number of seats: "))

## Formula: 
P = factorial(N) // factorial(N-R)

print("Total possible arrangements are:", P)







