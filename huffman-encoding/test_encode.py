'''
Created on Jun 16, 2023

@author: thomasvandrunen
'''

from huffman_trees import Leaf, Internal
from huffman import encode

def test_one_left():
    assert encode('x', Internal(Leaf('x',1),Leaf('y',1))) == '0'
    
def test_one_right() :
    assert encode('y', Internal(Leaf('x',1),Leaf('y',1))) == '1'
    
def test_slant() :
    tree = Internal(Internal(Internal(Leaf('a',1), 
                                                  Leaf('b',1)),
                                         Leaf('c',1)),
                                Leaf('d',1))
    assert encode('a', tree) == '000'
    assert encode('b', tree) == '001'
    assert encode('c', tree) == '01'
    assert encode('d', tree) == '1'
    
def test_even() :
    tree = Internal(Internal(Internal(Leaf('a',1), Leaf('b',1)), 
                             Internal(Leaf('c',1), Leaf('d',1))),
                    Internal(Internal(Leaf('e',1), Leaf('f',1)), 
                             Internal(Leaf('g',1), Leaf('h',1))))
    assert encode('a', tree) == '000'
    assert encode('b', tree) == '001'
    assert encode('c', tree) == '010'
    assert encode('d', tree) == '011'
    assert encode('e', tree) == '100'
    assert encode('f', tree) == '101'
    assert encode('g', tree) == '110'
    assert encode('h', tree) == '111'
    
def test_example() :
    tree = Internal(Internal(Leaf(' '),Internal(Leaf('A'),Internal(Leaf('T'),Leaf('R')))),Internal(Internal(Leaf('S'),Internal(Internal(Internal(Leaf('F'),Leaf('C')),Leaf('O')),Internal(Internal(Leaf('P'),Leaf('W')),Internal(Leaf('U'),Leaf('L'))))),Internal(Internal(Leaf('E'),Internal(Leaf('N'),Internal(Leaf('D'),Internal(Leaf('M'),Leaf('B'))))),Internal(Leaf('I'),Leaf('H')))))
    assert encode(' ', tree) == '00'
    assert encode('A', tree) == '010'
    assert encode('I', tree) == '1110'