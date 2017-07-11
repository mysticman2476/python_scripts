import os.path

PATH='./file.txt'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "File exists and is readable"
else:
    print "Either file is missing or is not readable"
