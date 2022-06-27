# Check Anagram, i,e (eat = ate) which contains similar words.

def check_anagram(st1, st2):
    if sorted(st1) == sorted(st2):
        print("The 2 strings are anagram")
        print("{} and {} are anagram".format(st1,st2))
        out = True
    else:
        print("{} and {} are not anagram".format(st1,st2))
        out = False
    return out

st1 = input("Enter 1st string: ")
st2 = input("Enter 2nd string: ")
print(check_anagram(st1,st2))
