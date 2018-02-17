
'''
Replace the class name in a file
'''
import re

# open text file
textFile = open('sample.html', 'r')

# string of text
fileContents = textFile.read()

# new class name
newClass = 'class="new-nav"'

# phone number regex
classRegex = re.compile('class="nav-link"')
classString = classRegex.sub(newClass, fileContents)

# write results to new file
outFile = open('sampleOut.html', 'w')
outFile.write(classString) 

# close files
textFile.close()
outFile.close()