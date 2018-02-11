
'''
Replace http with https in a file
Output results to a new file
'''
import re

# open text file
textFile = open('sample.txt', 'r')

# string of text
fileContents = textFile.read()

# phone number regex
httpRegex = re.compile('http:')
httpsString = httpRegex.sub('https:', fileContents)

# write results to new file
outFile = open('sampleOut.txt', 'w')
outFile.write(httpsString) 

# close files
textFile.close()
outFile.close()