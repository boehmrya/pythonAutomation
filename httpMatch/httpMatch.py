

import pyperclip, re

# phone number regex
httpsRegex = re.compile(r'''(
	(http|https)				# base http
	(://)				# first 3 digits
	(www\.)?				# optional www.
	([a-zA-z]+)			# any number of characters for domain name
	(\.) 				# dot before com/org/net
	(com|org|net) 		# com/org/net
	)''', re.VERBOSE)


# find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in httpsRegex.findall(text):
	url = ''.join([groups[1], groups[2], groups[3], groups[4], groups[5], groups[6]])
	matches.append(url)


# copy results to clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard: ')
	print('\n'.join(matches))
else:
	print('No urls found')

