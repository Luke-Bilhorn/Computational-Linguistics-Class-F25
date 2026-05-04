'''
Created on Jul 10, 2023

@author: thomasvandrunen
'''

from huffman import make_tree_from_text, encode_text, decode

def help_test(text, size):
    tree = make_tree_from_text(text)
    encoded = encode_text(text, tree)
    assert len(encoded) == size
    assert decode(encoded, tree) == text

def test_two_chars() :
    help_test('AAAAAAAH', 8)
    
def test_word() :
    help_test('breakfast', 27)
    
def test_short_phrase() :
    help_test('and so to business', 59)
    
def test_sentences() :
    help_test('Asteroids do not concern me. I want that ship, not excuses.', 238)
    
def test_warning() :
    help_test('TO STOP THE TRAIN IN CASE OF AN EMERGENCY PULL ON THE CHAIN PENALTY FOR IMPROPER USE FIVE POUNDS', 383)

def test_song() :
    help_test("The fascinating witches with the scintillating stiches on the britches of the boys who put the powder on the noses on the faces of the ladies of the harem of the course of King Caractacus were just passing by.",
              853)



    