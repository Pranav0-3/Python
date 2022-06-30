n = int(input("Enter your count: "))
l = []

for i in range(n):
    l.append(int(input("Enter digits: ")))

min_element = l[0]
max_element = l[0]

for element in l:
    if element > max_element:
        max_element = element
    if element < min_element:
        min_element = element

print("MAX:", max_element)
print("MIN:", min_element)
