# huffman.py
import sys

class Huffman:

    # Initialize Huffman instance
    #       
    # == TO DO ==
    #  - set up error handling for fileIO
    def __init__(self,inputFile,outputFile):
        self.inputFile = self.readFile(inputFile)
        self.outputFile = open(outputFile,'x')

    def generateFreqTable(self):
        dict = {}

        while True:
            c = self.inputFile.read(1)
            if c is '':
                return dict
            isRepeat = True if dict[c]

        return 

    def readFile():
        return

file = open(sys.argv[1])
print(file.read(1))
print(file.read(1))
print(file.read(1))
print(file.read(1))