import sys
import os

def readInputFile(inputFile = None):
    if inputFile == None:
        print ('Unable to fine input file!')
        sys.exit()

    fp = open(inputFile)
    lines = fp.readlines()
    fp.close()
    return lines
