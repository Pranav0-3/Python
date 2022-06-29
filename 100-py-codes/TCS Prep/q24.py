# read a word and letter from the console. Print the word after deleting all the occurance of the latter.
# EG Moon o
# op Mn


letter = input("Enter a word: ")
word = input("Enter a word to remove: ")

new = letter.replace(word, '')

print(new)