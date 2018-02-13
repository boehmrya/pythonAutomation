

import re

def strip(text, chars=""):
	if len(chars) > 0: # if characters to remove
		for ch in chars:
			charRegex = re.compile(ch)
			text = charRegex.sub("", text)
	else:
		startWhiteSpaceRegex = re.compile(r'^[ \t\n\r\f\v]+')
		endWhiteSpaceRegex = re.compile(r'[ \t\n\r\f\v]+?')
		text = startWhiteSpaceRegex.sub("", text)
		text = endWhiteSpaceRegex.sub("", text)
	return text


inputText = input("Enter a string to strip: ")
print(strip(inputText))