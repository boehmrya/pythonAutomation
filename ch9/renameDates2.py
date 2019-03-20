
import shutil, os, re

'''
Change European-style dates to American-style dates in file names.
'''

# create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?)    # all text before the date
    ((0|1|2|3)?\d)-     # one or two digits for the day
    ((0|1)?\d)-         # one or two digits for the month
    ((19|20)\d\d)       # four digits for the year
    (.*?)$                # all text after the date
    """, re.VERBOSE)

for euroFilename in os.listdir('sample2'):
    mo = datePattern.search(euroFilename)

    if mo == None:
        continue

    beforePart  = mo.group(1)
    dayPart   = mo.group(2)
    monthPart     = mo.group(4)
    yearPart    = mo.group(6)
    afterPart   = mo.group(8)

    # Form the European-style filename.
    amerFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('sample2')
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    amerFilename = os.path.join(absWorkingDir, amerFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (euroFilename, amerFilename))
    shutil.move(euroFilename, amerFilename)
