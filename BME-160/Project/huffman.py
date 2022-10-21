#!/usr/bin/env python3 
# Name: Simon Lee (siaulee) & Mateo Etcheveste (metcheve)
'''
A module that compresses Covid genome data using the Huffman Compression algorithm
'''

__author__ = 'Simon Lee, siaulee@ucsc.edu', 'Mateo Etcheveste, metcheve@ucsc.edu'

import heapq # import for min heap data structure
import os

class HuffmanCoding:
    '''
    Class that runs the huffman compression algorithm
    '''
    def __init__(self, path):
        '''
        Constructor Method for building a huffman coding 
        '''
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse = {}

    class HeapNode:
        '''
        We need a heap data structure for binary tree construction
        '''
        def __init__(self, char, freq):
            '''
            Constructor for heap data structure and definition of a node
            '''
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

		# defining comparators less_than and equals
        def __lt__(self, other):
            '''
            Special method that defines the behaviour of the less-than-or-equal-to operator <=. Important in tree construction
            '''
            # need a comparison function to make sure min heap stays ordered for proper tree construction
            return self.freq < other.freq
        
        def __eq__(self, other):
            '''
            Special method that defines the behaviour of the equal to operator ==. Important in tree construction
            '''
            # this function is needed incase two nodes have same length
            if(other == None):
                return False
            if(not isinstance(other, HeapNode)):
                return False
            return self.freq == other.freq

	# functions for compression:

    def histogram(self, txtfile):
        '''
        Constructs a histogram table of all characters and how many times they occur
        '''
        # counts all unique characters and assigns dictionary value with the count
        freq = {}
        for char in txtfile:
            if not char in freq:
                freq[char] = 0
            freq[char] += 1
        return freq

    def make_heap(self, freq):
        '''
        Constructs nodes needed for tree construction
        '''
        for key in freq:
            node = self.HeapNode(key, freq[key]) # creates a node for every unique character in file
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        '''
        Joins together nodes to construct trees
        '''
        while(len(self.heap)>1):
            # pops out the two nodes with lowest frequencies 
            nodeLeft = heapq.heappop(self.heap) 
            nodeRight = heapq.heappop(self.heap)

            # update the init of the new node from the heap data structure
            merged = self.HeapNode(None, nodeLeft.freq + nodeRight.freq)
            merged.left = nodeLeft
            merged.right = nodeRight

            heapq.heappush(self.heap, merged) # push node back to min heap


    def make_codes_helper(self, root, codeCurrent):
        '''
        Makes binary codes that performs like a lookup table to compress and decompress characters
        '''
        # recursive function that keeps traversing down a tree and every time it goes left records 0, go right records 1.
        if(root == None):
            return
        
        # checks if we can traverse further down the tree
        if(root.char != None): 
            self.codes[root.char] = codeCurrent
            self.reverse[codeCurrent] = root.char
            return

        # adds associted code if went left or right
        self.make_codes_helper(root.left, codeCurrent + "0")
        self.make_codes_helper(root.right, codeCurrent + "1")

    
    def make_codes(self):
        '''
        Makes binary codes that performs like a lookup table to compress and decompress characters
        '''
        # a function that just calls the method of building codes
        root = heapq.heappop(self.heap)
        codeCurrent = ""
        self.make_codes_helper(root, codeCurrent)


    def get_encoded_text(self, txtfile):
        '''
        Translates text into encoded code bits 
        '''
        encoded_txt = ""
        for char in txtfile:
            encoded_txt += self.codes[char]
        return encoded_txt


    def pad_encoded_text(self, encoded_text):
        '''
        Packs all bits into bytes for writing
        '''
        extra = 8 - len(encoded_text) % 8
        for i in range(extra):
            encoded_text += "0"

        info = "{0:08b}".format(extra)
        encoded_text = info + encoded_text
        return encoded_text


    def get_byte_array(self, encodedText):
        '''
        Prepares for writing bytes 
        '''
        # all text has to be a modulus of 8 or else we cannot write out properly and will lose information
        if(len(encodedText) % 8 != 0):
            print("Not a byte... Error!!!")
            exit(0)

        # gets all bits into a byte for writing purposes
        b = bytearray()
        for i in range(0, len(encodedText), 8):
            byte = encodedText[i:i+8]
            b.append(int(byte, 2))
        return b

    
    def encode(self):
        '''
        generates a binary file and compresses original file through traversing binary tree
        '''
        # extract the text and prepare for writing out to a .bin file
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        
        # were gonna read in text and 'wb' means writing binary out
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            txtfile = file.read()
            txtfile = txtfile.rstrip()

            # make histogram, then nodes, then tree, then codes
            freq = self.histogram(txtfile)
            self.make_heap(freq)
            self.merge_nodes()
            self.make_codes()

            # prepare for writing in .bin file by preparing bits to bytes
            encoded_text = self.get_encoded_text(txtfile)
            encodedText = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(encodedText)
            output.write(bytes(b))
        return output_path, self.codes


    """ functions for decompression """


    def padding(self, encodedText):
        info = encodedText[:8]
        extra = int(info, 2)

        encodedText = encodedText[8:] 
        encoded_text = encodedText[:-1*extra]

        return encoded_text

    def decode_text(self, encoded_text):
        '''
        Traverses binary tree to get text
        '''
        codeCurrent = ""
        decoded_text = ""

        # traverse down reconstructed tree and follow the tree until you have a tree with no child nodes. Then obtain character based on codes table
        for bit in encoded_text:
            codeCurrent += bit
            if(codeCurrent in self.reverse):
                character = self.reverse[codeCurrent]
                decoded_text += character
                codeCurrent = ""

        return decoded_text


    def decode(self, input_path):
        '''
        Actual decoding, going bit by bit to decode everything
        '''
        # take .bin file and write out to a _decompressed.txt file
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        # this time we read in binary and write out to normal text
        # traverses tree and decodes based off reconstructed tree
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.padding(bit_string)
            decompressed_text = self.decode_text(encoded_text)
            output.write(decompressed_text)

        return output_path


def encode(huffman):
    '''
    calls the method for encoding in the huffman class and generates a binary file
    '''
    output_path, codes = huffman.encode()
    return output_path, codes

def decode(huffman, file):
    '''
    calls the method from the huffman class and decodes our binary file
    '''
    huffman.decode(file)

def printCodes(codes_dict, file):
    '''
    This function prints the codes very nicely
    '''
    # print codes 
    file.write(' Char | Huffman code \n')
    file.write('----------------------\n')
    for key, value in codes_dict.items():
        file.write((' %-4r |%12s' % (key, value)))
        file.write("\n")


import time
import sys

start_time = time.time()
def main():
    '''
    Driver of the code
    '''
    path = sys.argv[1] # takes in arguments from command line
    h = HuffmanCoding(path) # constructs a huffman object
    compressed, codes = encode(h) # encode our text, generates a binary file with compression of original text
    file1 = open('Histogram.txt', 'w') # write out the codes to the text
    printCodes(codes, file1) 
    file1.close()
    decode(h, compressed) # decompresses binary file into original text
    
    # Compression Stats
    file_size_encode = os.stat(compressed)
    file_size_decode = os.stat(path)

    # Printing statistics to see effectiveness of compression
    print("Size of uncompressed file :"
          , file_size_decode.st_size, "bytes,", 
          round(int(file_size_decode.st_size)/1000000, 4),"megabytes,", round(int(file_size_decode.st_size)/1000000000, 4), "Gigabytes")
    print("  Size of compressed file :", file_size_encode.st_size, "bytes,",           round(int(file_size_encode.st_size)/1000000, 4),"megabytes,",round(int((file_size_encode.st_size)/1000000000), 4), "Gigabytes")
    print("            Compressed by :",round(((1 - (file_size_encode.st_size/file_size_decode.st_size)) * 100),2), "%")
    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    '''
    Run code 
    '''
    main()