'''
Created on Jun 7, 2023

@author: thomasvandrunen
'''

from huffman_trees import Leaf, Internal
from functools import reduce #was _functools
from collections import Counter

def encode(c, key):
    assert key.contains(c)
    bits = ''
    #! invariant: key.contains(c)
    #! Populate bits with 0s and 1s

    #while true
        #if isInstance(key, Leaf)
            #break
        #if key.left.contains(c)
            #key = key.left
            #bits = bits + '0'
        #if key.right.contains(c)
            #key = key.right
            #bits = bits + '1'
        #else 
            #assert that this cannot happen

    while True:
        if isinstance(key, Leaf):
            break
        elif key.left.contains(c):
            key = key.left
            bits = bits + '0'
        elif key.right.contains(c):
            key = key.right
            bits = bits + '1'
        else:
            assert 1 == 0
            #Theoretically, this case could be used to detect a character boundary.
            #But, what if he gives me a character that isn't in the encoding?
            #That has to be accounted for. 

    return bits

#! This function encodes an entire string by applying the above
#! encode() function. You should think through this and make
#! sure you understand how it works. The reduce() function 
#! is like the foldl function you learned in CSCI 243
def encode_text(text, key):
    return reduce(lambda rest, c: rest + encode(c, key), text, '')

def decode(bits, key):
    msg = ''
    current = key
    #! invariant: isinstance(current, Internal) 
    #! Populate msg

    while len(bits) > 0:
        #put the if current is a leaf stuff up here instead?
        bit, bits = bits[0], bits[1:]
        assert bit == '0' or bit == '1'
        current = current.left if bit == '0' else current.right
        if isinstance(current, Leaf):
            msg = msg + current.c
            current = key


    #while bits has characters left in it
        #remove the first digit of bits and update current to current.left or current.right based on the value (0 or 1)
        #If current is a leaf (if current has no children?)
            #add this character to msg
            #reset current to key
    return msg

def make_tree_from_leaves(nodes):
    #sort the list by frequency
    #while there is more than one node in the list
        #put the last two nodes in the list together into a new internal
        #sort the list by frequency
    #return that last node

    #sort_nodes_by_frequency(nodes)
    while len(nodes) > 1:
        #could just move the frequency sort here for a single call?
        #sort_nodes_by_frequency(nodes)
        nodes.sort(key=lambda node: -1*node.total_freq())
        nodes = nodes[:-2] + [Internal(nodes[-2], nodes[-1])]
        #sort_nodes_by_frequency(nodes)

    return nodes[0]

#def sort_nodes_by_frequency(nodes):
    #nodes.sort(key=lambda node: -1*node.total_freq())
    #return nodes

def make_tree_from_text(text):
    #text to list of characters
    #use count(?) to make a dictionary of chars and freqs
    #make each of these into leaves, in a list
    #return this
    
   # a = Counter(list(text))
    #print(Counter(text).most_common())
    #print(["k:{"+ str(k) + "};v:{" + str(v) + "} " for (k, v) in a.items()])

    #b = Leaf('A', 4)
    #print(str(b) + "\n")
    #print(["(" + char + ", " + freq + ")" for (char, freq) in Counter(text).most_common()])
    return make_tree_from_leaves([Leaf(char, freq) for (char, freq) in Counter(text).most_common()])

    #pass
