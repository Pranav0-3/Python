# read the word and print the longest repeating character.
# ERROR


word = input("Enter a word/sentence: ")
count = 1
max_count = 0

for i in range(len(word)-1):
    if word[i] == word[i+1]:
        print(word[i],word[i+1])
        count += 1

    else:
        max_count = max(max_count,count)
        count = 1
        max_count = max(max_count,count)
        if  max_count > 1:
            print(max_count)
