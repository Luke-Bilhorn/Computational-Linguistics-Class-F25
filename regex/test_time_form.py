'''
Created on May 31, 2023

@author: thomasvandrunen
'''

import re
from regexercises import time_format

def test_valid_a():
    assert time_format('03:25 AM')

def test_valid_b():
    assert time_format('06:01 PM')

def test_valid_c():
    assert time_format('07:00 AM')

def test_valid_d():
    assert time_format('11:59 PM')

def test_valid_e():
    assert time_format('12:30 PM')

def test_valid_f():
    assert time_format('10:05 AM')

def test_valid_g():
    assert time_format('I want us to be ready to leave by 10:15 AM, okay?')



def test_invalid_a():
    assert not time_format('3:25 AM')

def test_invalid_b():
    assert not time_format('13:25 AM')

def test_invalid_c():
    assert not time_format('03:25 XM')

def test_invalid_d():
    assert not time_format('03:25 am')

def test_invalid_e():
    assert not time_format('10:5 AM')

def test_invalid_f():
    assert not time_format('010:15 AM')
    
def test_invalid_g():
    assert not time_format('09:005 AM')

def test_invalid_h():
    assert not time_format('09:150 AM')

def test_invalid_i():
    assert not time_format('09:233 AM')

def test_invalid_j():
    assert not time_format('09:000 AM')
    
def test_invalid_k():
    assert not time_format('11:60 PM')
    
def test_invalid_l():
    assert not time_format('09:65 AM')

def test_invalid_m():
    assert not time_format('09:305 AM')

def test_invalid_n():
    assert not time_format('09:35 AMM')



