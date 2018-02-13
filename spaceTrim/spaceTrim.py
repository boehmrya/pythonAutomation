
import re

# social security number regex
whiteSpaceRegex = re.compile(r'[ \t\n\r\f\v]+')

# open text file
textFile = open('sample.txt', 'r')

# string of text for contents of file
text = textFile.read()

# replace multiple white spaces with a single white space
text = whiteSpaceRegex.sub(" ", text)

# write results to new file
outFile = open('sampleOut.txt', 'w')
outFile.write(text) 

# close files
textFile.close()
outFile.close()

