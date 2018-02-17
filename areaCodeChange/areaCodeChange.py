
import re

'''
Find each phone number
Change area code from 319- to (319) format
'''

# regex for m/dd/yyyy
phoneRegex = re.compile(r'''(
	([0-9]{3})		# area code
	(-)
	([0-9]{3})		# first 3 digits in phone number
	(-)
	([0-9]{4})		# last 4 digits in phone number
	)''', re.VERBOSE)


# open text file
textFile = open('sample.txt', 'r')


# string of text
text = textFile.read()


# find matches for first regex
for groups in phoneRegex.findall(text):
	#print(groups)
	newPhoneNum = '(' + groups[1] + ') ' + ''.join([groups[3], groups[4], groups[5]])
	newPhoneRegex = re.compile(groups[0])
	text = newPhoneRegex.sub(newPhoneNum, text)


# write results to new file
outFile = open('sampleOut.txt', 'w')
outFile.write(text) 


# close files
textFile.close()
outFile.close()





