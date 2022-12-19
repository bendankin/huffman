# huffman.py
import sys

class Huffman:

    # Initialize Huffman instance
    #       
    # == TO DO ==
    #  - set up error handling for fileIO
    def __init__(self,inputFile,outputFile):
        self.inputFile = open(inputFile)
        self.outputFile = open(outputFile,'w')
        self.freqTable = self.genFreqTable()
            

    # Create a frequency table for the initialized input file
    def genFreqTable(self):
        dict = {}

        while True:
            c = self.inputFile.read(1)
            if c == '':
                return dict
            try:
                dict[c]+=1
            # if c does not exist in the table yet then create a new index
            except KeyError:
                dict[c]=1
    
    # Create a Huffman code tree for the initialized input file
    def genHuffmanCode(self):

        return



h = Huffman(sys.argv[1],"fqwedqw")
c = h.genFreqTable()
print(c)