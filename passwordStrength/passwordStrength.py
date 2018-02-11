
import re

# social security number regex
minEightRegex = re.compile(r'\w{8,}')	# minimum eight chars
oneLetterRegex1 = re.compile(r'[a-z]+')	# at least one lowercase letter
oneLetterRegex2 = re.compile(r'[A-Z]+')	# at least one uppercase letter
oneNumberRegex = re.compile(r'\d+')		# at least one number 

# string of text for contents of file
password = input("Enter a password: ")

length = minEightRegex.search(password)
lowCaseLetters = oneLetterRegex1.search(password)
upCaseLetters = oneLetterRegex2.search(password)
number = oneNumberRegex.search(password)

if (length != None) and (lowCaseLetters != None) and (upCaseLetters != None) and (number != None):
	print("strong")
else:
	print("not strong")





