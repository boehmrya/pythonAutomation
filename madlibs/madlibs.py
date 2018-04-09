

# open a files
f = open('sample.txt')
contents = f.read()
words = contents.split()

# replace the words
count = 0
for w in words:
    if w == 'ADJECTIVE':
        newWord = input("Enter an adjective: ")
        words[count] = newWord
    elif w == 'ADVERB':
        newWord = input("Enter an adverb: ")
        words[count] = newWord
    elif w == 'VERB':
        newWord = input("Enter an verb: ")
        words[count] = newWord
    elif w == 'NOUN':
        newWord = input("Enter an noun: ")
        words[count] = newWord
    count += 1

# write the final contents
newContents = ' '.join(words)
out = open("out.txt","w")
out.write(newContents)
