
import re
import os

# get the regex pattern from user
userRegexString = input("Enter a regex pattern: ")
userRegex = re.compile(userRegexString)

# loop through each file in directory and open it
for filename in os.listdir():
    if filename.endswith('.txt'):
        f = open(filename)
        text = f.read()

        # find matches pattern and print to screen
        for groups in userRegex.findall(text):
        	print(groups)
