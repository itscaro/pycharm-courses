import csv
import os
import random

def readFile(filepath):
    """
    Read the input CSV file
    :param filepath:
    :return list: list of entries in the csv
    """
    with open(filepath, 'r') as fileHandler:
        reader = ''

def writeFile(filepath, result):
    """
    Write out to CSV file
    :param filepath:
    :param result:
    :return:
    """
    with open(os.path.dirname(filepath) + '/result.csv', 'w') as fileHandler:
        writer = ''

def calculateForEachCategory(input):
    """
    Do the calculate
    :return list: list of the calculated amounts for each category
    """

def printOut(input):
    """
    Print out the result as asked
    :param input:
    :return:
    """

while True:
    filepath = input('Gimme the file path: ')
    if os.path.isfile(filepath):
        input = readFile(filepath)
        result = calculateForEachCategory(input)
        printOut(result)
        writeFile(filepath, result)
        break
    else:
        print('I cannot find the file "%s"' % filepath)

