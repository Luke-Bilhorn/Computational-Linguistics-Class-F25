'''
Program to test the HMM 

Created on Aug 22, 2013

@author: tvandrun
'''

import numpy as np
import nltk 
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from hmm_tagger import HMMTagger


DEBUG = False

# Location of the training text (the Federalist papers)
corpus_root = '.' #'/homes/tvandrun/Public/cs384/federalist'
corpus_file = 'federalist-all.txt'

# The test set is a ~780 word portion with no hapaxes.
# This appears as lines 15214-15282 in the file itself
test_begin = 166979
test_end = 167762

# Load the corpus
corpus_reader = PlaintextCorpusReader(corpus_root, '.*')
print("Loading corpus...")
corpus_all =  [w.lower() for w in nltk.Text(corpus_reader.words(corpus_file)) 
               if not w.isnumeric()]

# Separate the training and test texts
training_text = corpus_all[:test_begin] + corpus_all[test_end:]
test_text = corpus_all[test_begin:test_end]

# Find the set of types
print("Collating vocabulary...")
vocab = set(training_text)
print(len(vocab))

# Tag the training text using NLTK's own tagger
print("Tagging training set...")
training_tagged = nltk.pos_tag(training_text, tagset='universal')

# Train the tagger
print("Training tagger...")
tagger = HMMTagger(training_tagged, vocab)
tagger.sanity_check()  

# Tag the test set with our tagger
print("Tagging test set with trained tagger...")
test_tagged = tagger.pos_tag(test_text)

# Computing accuracy by comparing our tagging with NLTK's
test_tagged_compare = nltk.pos_tag(test_text, tagset='universal')
acc = np.mean([test_tagged[i][1] == test_tagged_compare[i][1] 
               for i in range(len(test_text))])
print("Accuracy: " + str(acc*100) + "%")

# Print tags that our tagger gets wrong
if DEBUG :
    for i in range(len(test_text)) :
        assert test_text[i] == test_tagged[i][0]
        assert test_text[i] == test_tagged_compare[i][0]
        if test_tagged[i][1] != test_tagged_compare[i][1] :
            print(test_text[i], test_tagged[i][1], test_tagged_compare[i][1])



