
'''
Replace <p> tags with <div> tags
'''

import re

# open text file
textFile = open('sample.html', 'r')

# string of text
fileContents = textFile.read()

# regex for opening tag
openTagRegex = re.compile('<p')

# regex for closing tag
closedTagRegex = re.compile('</p')

# replace opening tag, which could have attributes
newContents = openTagRegex.sub('<div', fileContents)
newContents = closedTagRegex.sub('</div', newContents)

# write results to new file
outFile = open('sampleOut.html', 'w')
outFile.write(newContents) 

# close files
textFile.close()
outFile.close()