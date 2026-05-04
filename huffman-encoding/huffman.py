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
    return bits

def encode_text(text, key):
    return reduce(lambda rest, c: rest + encode(c, key), text, '')

def decode(bits, key):
    msg = ''
    current = key
    while len(bits) > 0:
        bit, bits = bits[0], bits[1:]
        assert bit == '0' or bit == '1'
        current = current.left if bit == '0' else current.right
        if isinstance(current, Leaf):
            msg = msg + current.c
            current = key
    return msg

def make_tree_from_leaves(nodes):
    while len(nodes) > 1:
        nodes.sort(key=lambda node: -1*node.total_freq())
        nodes = nodes[:-2] + [Internal(nodes[-2], nodes[-1])]
    return nodes[0]

def make_tree_from_text(text):
    return make_tree_from_leaves([Leaf(char, freq) for (char, freq) in Counter(text).most_common()])