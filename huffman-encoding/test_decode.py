'''
Created on Jun 16, 2023

@author: thomasvandrunen
'''

from huffman_trees import Leaf, Internal
from huffman import decode

def test_one_left():
    assert decode('0', Internal(Leaf('x',1),Leaf('y',1))) == 'x'
    
def test_one_right() :
    assert decode('1', Internal(Leaf('x',1),Leaf('y',1))) == 'y'
    
def test_slant() :
    tree = Internal(Internal(Internal(Leaf('a',1), 
                                                  Leaf('b',1)),
                                         Leaf('c',1)),
                                Leaf('d',1))
    assert decode('000', tree) == 'a'
    assert decode('001', tree) == 'b'
    assert decode('01', tree) == 'c'
    assert decode('1', tree) == 'd'
    
def test_even() :
    tree = Internal(Internal(Internal(Leaf('a',1), Leaf('b',1)), 
                             Internal(Leaf('c',1), Leaf('d',1))),
                    Internal(Internal(Leaf('e',1), Leaf('f',1)), 
                             Internal(Leaf('g',1), Leaf('h',1))))
    assert decode('000', tree) == 'a'
    assert decode('001', tree) == 'b'
    assert decode('010', tree) == 'c'
    assert decode('011', tree) == 'd'
    assert decode('100', tree) == 'e'
    assert decode('101', tree) == 'f'
    assert decode('110', tree) == 'g'
    assert decode('111', tree) == 'h'
    
def test_example() :
    tree = Internal(Internal(Leaf(' '),Internal(Leaf('A'),Internal(Leaf('T'),Leaf('R')))),Internal(Internal(Leaf('S'),Internal(Internal(Internal(Leaf('F'),Leaf('C')),Leaf('O')),Internal(Internal(Leaf('P'),Leaf('W')),Internal(Leaf('U'),Leaf('L'))))),Internal(Internal(Leaf('E'),Internal(Leaf('N'),Internal(Leaf('D'),Internal(Leaf('M'),Leaf('B'))))),Internal(Leaf('I'),Leaf('H')))))
    assert decode('11101010000001101111111010000111010000010001010011010111010100101110101111010011100100111111101011000001101111110011010001011011111110001111100001110100000110111111000001011011101101111010100100010110110101010111', tree) == 'IF THIS IS A CONSULAR SHIP THEN WHERE IS THE AMBASSADOR'
