
import shutil, os

for filename in os.listdir('sample2'):

    prefix = 'spam'

    # Form the European-style filename.
    newFilename = prefix + filename

    # Get the full, absolute file paths.
    absFilesDir = os.path.abspath('sample2')
    oldFilename = os.path.join(absFilesDir, filename)
    newFilename = os.path.join(absFilesDir, newFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (oldFilename, newFilename))
    shutil.move(oldFilename, newFilename)
