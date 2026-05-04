'''
Created on May 31, 2023

@author: thomasvandrunen
'''

from regexercises import convert_date_format

def test_one_date():
    assert convert_date_format('07-06-1977') == '06.07.1977'

def test_date_in_sentence() :
    assert (convert_date_format('Harry Potter was born on 07-31-1980, one day after Neville Longbottom.')
            == 'Harry Potter was born on 31.07.1980, one day after Neville Longbottom.')

def test_no_date() :
    assert (convert_date_format("There don't seem to be any dates in this sentence.") 
            == "There don't seem to be any dates in this sentence.") 
    
def test_range() :
    assert (convert_date_format('Alexander Hamilton was Secretary of the Treasury from 09-11-1789 to 01-31-1795.')
            == 'Alexander Hamilton was Secretary of the Treasury from 11.09.1789 to 31.01.1795.')
    
def test_several_dates() :
    assert (convert_date_format('The dates of crewed moon landings were 07-20-1969, 11-19-1969, 02-06-1971, 08-02-1971, 04-24-1972, and 12-14-1972.') ==
            'The dates of crewed moon landings were 20.07.1969, 19.11.1969, 06.02.1971, 02.08.1971, 24.04.1972, and 14.12.1972.')