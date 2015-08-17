import csv
import os
import random

the_list = []
for i in range(0, 15):
    the_list.append(round(random.uniform(-100.0, 100.0), 2))

with open('result.csv', 'w') as fileHandler:
    # By default the "lineterminator" argument is "\r\n", here we need to change it to "\n"
    # By default the "delimiter" argument is ",", here we need to change it to ";"
    writer = Ger a CSV writer
    writer.Write the header line with a list of "Key" and "Value" as items
    Write into the CSV file

print("The file '%s' was created in '%s'" % ('result.csv', os.path.dirname(os.path.realpath(__file__))))
