# count number of prime numbers in list from user
# ERROR

n = int(input("Enter your count: "))
l = []

for i in range(n):
    l.append(int(input("Enter the nums: ")))

    prime_count = 0
    for element in l:
        if element == 1 or element == 0:
            continue
        else:
            prime = True

            for number in range(2,element):
                if element%number == 0:
                    prime = False

                if prime == True:
                    prime_count += 1    

    print(f"There are {prime_count} nos. of prime in list")
