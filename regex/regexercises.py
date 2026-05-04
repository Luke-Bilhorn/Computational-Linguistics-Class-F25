'''
Created on May 30, 2023

@author: thomasvandrunen
'''

import re

def time_format(time):
     return re.search(r"\b(?:0[1-9]|1[0-2]):[0-5][0-9] (A|P)M\b", time) != None

def suffix_stemmer(suf):
     return r"\b(\w{3,})" + suf + r"\b"

def convert_date_format(msg):
     return re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\2.\1.\3", msg)
     #r = re.search(r"(?P<front>.*?)(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})(?P<back>.*)", msg)
     #return r.group("front") + r.group("day") + "." + r.group("month") + "." + r.group("year") + r.group("back") if r != None else msg