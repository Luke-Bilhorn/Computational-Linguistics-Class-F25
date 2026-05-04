'''
Created on Jul 7, 2023

@author: thomasvandrunen
'''

from huffman_trees import Leaf, Internal
from huffman import encode_text, make_tree_from_leaves

def test_one():
    n = Leaf('q')
    assert make_tree_from_leaves([n]) == n

def test_two() :
    n = Leaf('y')
    m = Leaf('p')
    x = make_tree_from_leaves([n, m])
    assert x == Internal(n, m) or x == Internal(m, n)

def test_three() :
    a = Leaf('a', frequency=100)
    b = Leaf('b')
    c = Leaf('c')
    x = make_tree_from_leaves([b,c,a])
    assert (x == Internal(a, Internal(b,c)) or
            x == Internal(a, Internal(c, b)) or 
            x == Internal(Internal(b, c), a) or 
            x == Internal(Internal(c, b), a))
    
def test_length():
    nn = [Leaf("W",1),Leaf("P",1),Leaf("F",1),Leaf("R",1),Leaf("B",1),
         Leaf("M",1),Leaf("A",1),Leaf("L",1),Leaf("U",2),Leaf("K",2),
         Leaf("'",2),Leaf("N",3),Leaf("S",3),Leaf("G",3),Leaf("D",3),
         Leaf("O",3),Leaf("E",6),Leaf("H",7),Leaf("T",7),Leaf("I",9),Leaf(" ",14)]
    tree = make_tree_from_leaves(nn)
    text = "WHEN I SIGNED UP FOR THIS HIKE I THOUGHT IT'D BE SOMETHING THAT I'D LIKE"
    encoded_text = encode_text(text, tree) #reduce(lambda rest, c: rest + encode(c, tree), text, '')

    assert len(encoded_text) == 281
    
    