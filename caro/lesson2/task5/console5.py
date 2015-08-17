import csv
import os.path

while True:
    filepath = input('Gimme the file path: ')
    if os.path.isfile(filepath):
        break
    else:
        print('I cannot find the file "%s"' % filepath)

with open(filepath) as csvfile:
    # Use the keyword-argument delimiter=';' to set the field delimiter to ";"
    # To use a keyword-argument, you need to name the argument when passing it to the function/method, for example:
    # func(delimiter=";")
    reader = Read the "csvfile" file object with csv.reader(), remember to use the delimiter ";"

# You can replace
#
# with open(filepath) as csvfile:
#
# with
#
# csvfile = open(filepath)
#
# but remeber to close the file!
