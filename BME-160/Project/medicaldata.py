'''
A module that compresses medical patient data using the Huffman Compression algorithm
'''

__author__ = 'Simon Lee, siaulee@ucsc.edu'

import heapq
import os

class HuffmanCoding:
    def __init__(self, path):
        '''
        Constructor Method for building a huffman coding 
        '''
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        '''
        We need a heap data structure for binary tree construction
        '''
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

		# defining comparators less_than and equals
        def __lt__(self, other):
            '''
            Special method that defines the behaviour of the less-than-or-equal-to operator <=. Important in tree construction
            '''
            return self.freq < other.freq
        
        def __eq__(self, other):
            '''
            Special method that defines the behaviour of the equal to operator ==. Important in tree construction
            '''
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
        frequency = {}
        for character in txtfile:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        '''
        Constructs nodes needed for tree construction
        '''
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        '''
        Joins together nodes to construct trees
        '''
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)


    def make_codes_helper(self, root, current_code):
        '''
        Makes binary codes that performs like a lookup table to compress and decompress characters
        '''
        if(root == None):
            return
        
        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    
    def make_codes(self):
        '''
        Makes binary codes that performs like a lookup table to compress and decompress characters
        '''
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)


    def get_encoded_text(self, txtfile):
        '''
        Translates text into encoded code bits 
        '''
        encoded_text = ""
        for character in txtfile:
            encoded_text += self.codes[character]
        return encoded_text


    def pad_encoded_text(self, encoded_text):
        '''
        Packs all bits into bytes for writing
        '''
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text


    def get_byte_array(self, padded_encoded_text):
        '''
        Prepares for writing bytes 
        '''
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    
    def encode(self):
        '''
        
        '''
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            txtfile = file.read()
            txtfile = txtfile.rstrip()

            frequency = self.histogram(txtfile)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(txtfile)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
        return output_path, self.codes


    """ functions for decompression: """


    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text


    def decode(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)
            decompressed_text = self.decode_text(encoded_text)
            output.write(decompressed_text)

        return output_path

def encode(huffman):
    output_path, codes = huffman.encode()
    return output_path, codes

def decode(huffman, file):
    huffman.decode(file)

def printCodes(codes_dict, file):
    # print codes 
    file.write(' Char | Huffman code ')
    file.write('----------------------\n')
    for key, value in codes_dict.items():
        file.write((' %-4r |%12s' % (key, value)))
        file.write("\n")

import time
start_time = time.time()
def main():
    path = "/Users/simonlee/bme160-inspections/final-project/Simon/test.txt"
    h = HuffmanCoding(path)
    compressed, codes = encode(h)
    file1 = open('Histogram.txt', 'w')
    printCodes(codes, file1)
    file1.close()
    decode(h, compressed)
    
    # Compression Stats
    file_size_encode = os.stat(compressed)
    file_size_decode = os.stat(path)

    print("Size of uncompressed file :"
          , file_size_decode.st_size, "bytes,", 
          round(int(file_size_decode.st_size)/1000000, 4),"megabytes,", round(int(file_size_decode.st_size)/1000000000, 4), "Gigabytes")
    print("  Size of compressed file :", file_size_encode.st_size, "bytes,",           round(int(file_size_encode.st_size)/1000000, 4),"megabytes,",round(int((file_size_encode.st_size)/1000000000), 4), "Gigabytes")
    print("            Compressed by :",round(((1 - (file_size_encode.st_size/file_size_decode.st_size)) * 100),2), "%")
    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__":
    main()