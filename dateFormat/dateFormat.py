
import re

'''
Take any of these three formats
m/d/yyyy
yyyy/m/d
mm-dd-yyyy

Turn them all into the first format: m/dd/yyyy
'''

# regex for m/dd/yyyy
dateRegex1 = re.compile(r'''(
	([0-9]{1,2})		# month
	(/)
	([0-9]{1,2})		# day
	(/)
	([0-9]{4})			# year
	)''', re.VERBOSE)


# regex for yyyy/m/d
dateRegex2 = re.compile(r'''(
	([0-9]{4})			# year
	(/)
	([0-9]{1,2})		# month
	(/)
	([0-9]{1,2})		# day
	)''', re.VERBOSE)


# regex for mm-dd-yyyy
dateRegex3 = re.compile(r'''(
	([0-9]{2})		# month
	(-)
	([0-9]{2})		# day
	(-)
	([0-9]{4})		# year
	)''', re.VERBOSE)


# open text file
textFile = open('sample.txt', 'r')


# string of text
text = textFile.read()


# find matches for first regex
for groups in dateRegex1.findall(text):
	newDate1 = '/'.join([groups[1], groups[3], groups[5]])
	newDateRegex1 = re.compile(groups[0])
	text = newDateRegex1.sub(newDate1, text)


# find matches for second regex
for groups in dateRegex2.findall(text):
	newDate2 = '/'.join([groups[3], groups[5], groups[1]])
	newDateRegex2 = re.compile(groups[0])
	text = newDateRegex2.sub(newDate2, text)


# find matches for third regex
for groups in dateRegex3.findall(text):
	# pull off first digit on month
	if groups[1][0] == "0":
		group1 = groups[1][1]
	else:
		group1 = groups[1]

	# pull off first digit on day
	if groups[3][0] == "0":
		group3 = groups[3][1]
	else:
		group3 = groups[3]
	newDate3 = '/'.join([group1, group3, groups[5]])
	newDateRegex3 = re.compile(groups[0])
	text = newDateRegex3.sub(newDate3, text)


# write results to new file
outFile = open('sampleOut.txt', 'w')
outFile.write(text) 


# close files
textFile.close()
outFile.close()





