import shutil, os, re

'''
Remove all zeroes in file names.
'''

# create a regex that matches zeroes
zeroRegex = re.compile('0')

for filename in os.listdir('sample3'):
    newFilename = zeroRegex.sub('', filename)

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('sample3')
    oldFilename = os.path.join(absWorkingDir, filename)
    newFilename = os.path.join(absWorkingDir, newFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (oldFilename, newFilename))
    shutil.move(oldFilename, newFilename)
