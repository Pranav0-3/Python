# Maximum Number Of Handshakes in Python
# Here, in this page we will discuss the program to find the maximum number of handshakes in python.
# For the number of handshakes to be maximum, every person should handshake with every other person in the room 
# i.e. all persons present should shake hands.


# For the first person, there will be N-1 people to shake hands with
# For second person, there will be N -1 people available but as he has already shaken hands with the first person,
# there will be N-1-1 = N-2 shake-hands
# For third person, there will be N-1-1-1 = N-3, and So On…
# Therefore the total number of handshake   

#  FORMULA:  ( N – 1 + N – 2 +….+ 1 + 0 ) = (int( (N-1) * N ) / 2)



N = int(input("Enter the No. of People: "))
handshakes = int(((N-1)*N) / 2)

print("Total Handshakes done are:", handshakes)