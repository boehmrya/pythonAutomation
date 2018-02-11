
import re

# social security number regex
ssRegex = re.compile(r'''(
	(\s)
	([0-9]{3})		
	(-)
	([0-9]{2})		
	(-)
	([0-9]{4})		
	(\W+)	
	)''', re.VERBOSE)

# open text file
textFile = open('sample.txt', 'r')

# string of text for contents of file
text = textFile.read()

# mask each social security number with xxx-xx-xxxx
text = ssRegex.sub(" xxx-xx-xxxx ", text)

# write results to new file
outFile = open('sampleOut.txt', 'w')
outFile.write(text) 

# close files
textFile.close()
outFile.close()