# pattern matching qus for a given string.


str1 = input("Enter:")
str1 = str1.lower()
st2 = input()
st2 = st2.lower()
# NEED TO WORK FOR CASE INSENSITIVE :(

if str1.startswith(st2) or str1.endswith(st2):
    print("{} contains {}".format(str1,st2))
else:
    print("{} not contains {}".format(str1,st2))