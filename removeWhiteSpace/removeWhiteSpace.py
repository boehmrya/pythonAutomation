import re

# removes white space from an html file

# white space regex
whiteSpaceRegex = re.compile(r'[ \t\n\r\f\v]+')

# open text file
htmlFile = open('sample.html', 'r')

# string of text for contents of file
content = htmlFile.read()

# replace multiple white spaces with a single white space
newContent = whiteSpaceRegex.sub("", content)

# write results to new file
outFile = open('out.html', 'w')
outFile.write(newContent) 

# close files
outFile.close()
htmlFile.close()