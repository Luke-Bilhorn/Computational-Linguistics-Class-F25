'''
Created on May 30, 2023

@author: thomasvandrunen
'''

import re
from regexercises import suffix_stemmer

def test_ing_pos() :
    rr = suffix_stemmer('ing')
    assert re.search(rr, 'testing')

def test_ing_neg() :
    rr = suffix_stemmer('ing')
    assert not (re.search(rr, 'cardinal'))

def test_ing_stem() :
    w = 'testing'
    rr = suffix_stemmer('ing')
    m = re.search(rr, w)
    assert len(m.groups()) == 1
    assert m[0] == w
    assert m[1] == 'test'
    
def test_ing_part() :
    w = 'this is testing it'
    rr = suffix_stemmer('ing')
    m = re.search(rr, w)
    assert len(m.groups()) == 1
    assert m[0] == 'testing'
    assert m[1] == 'test'
    
def test_ing_many() :
    w = 'we go walking, hiking, biking, and seeing stuff'
    rr = suffix_stemmer('ing')
    m = re.findall(rr, w)
    assert len(m) == 4
    assert m[0] == 'walk'
    assert m[1] == 'hik'
    assert m[2] == 'bik'
    assert m[3] == 'see'

def test_not_ring() :
    rr = suffix_stemmer('ing')
    assert not (re.search(rr, 'sing'))
    assert not (re.search(rr, 'ring'))
    assert not (re.search(rr, 'wring'))
    
def test_one_vowel() :
    rr = suffix_stemmer('ing')
    assert re.search(rr, 'ebbing')
    assert re.search(rr, 'crying')
    
def test_ing_ing():
    rr = suffix_stemmer('ing')
    m = re.search(rr, 'ringing')
    assert len(m.groups()) == 1
    assert m[0] == 'ringing'
    assert m[1] == 'ring'

def test_ed() :
    rr = suffix_stemmer('ed')
    w = 'welded wedding'
    m = re.search(rr, w)
    assert len(m.groups()) == 1
    assert m[0] == 'welded'
    assert m[1] == 'weld'



