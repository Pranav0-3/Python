# pattern matching qus for a given string.


str = input("Enter:")
st2 = input()

# NEED TO WORK FOR CASE INSENSITIVE :(

if str.startswith(st2) or str.endswith(st2):
    print("{} contains {}".format(str,st2))
else:
    print("{} not contains {}".format(str,st2))