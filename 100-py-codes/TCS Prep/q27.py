# count the occurance of the word in a sentence and print it.


sent = input("Enter a sentence: ")
word = input("Enter the word to find its occurance: ")
sent = sent.lower()
word = word.lower()


count = sent.count(word)
print("The word {} has occured {} times.".format(word,count))