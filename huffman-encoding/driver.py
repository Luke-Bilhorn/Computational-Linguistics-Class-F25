'''
Created on Jun 14, 2023

@author: thomasvandrunen
'''

import sys
from huffman import encode_text, decode, make_tree_from_text
from _functools import reduce


text = sys.argv[1]

print('Original text: ' + text)

tree = make_tree_from_text(text)

print('Tree: ' + str(tree))

encoded_text = encode_text(text, tree) #reduce(lambda rest, c: rest + encode(c, tree), text, '')

print('Encoded text: ' + encoded_text)

print('Encoded text size: ' + str(len(encoded_text)) +  ' bits')

decoded_text = decode(encoded_text, tree)

print('Decoded text: ' + decoded_text)
