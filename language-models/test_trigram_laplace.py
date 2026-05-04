'''
Created on Jul 12, 2023

@author: thomasvandrunen
'''
from langmod import *
from perplexity import *
import re
import math
from lm_train import lm_data, corpus_path, training_vocab, held_out_text
from pytest import approx
from compress import Decompressor, compress_decompress_accuracy

test_file_name = corpus_path + "test-smallish.txt"


test_raw_words = re.findall(r'[a-z][a-z\']*|\d+|[!$%*()\-:;\"\',.?]', open(test_file_name).read().lower())
test_text = [transform(w) for w in test_raw_words]

model = TrigramLaplaceLanguageModel(lm_data)

def test_vocab() :
    assert vocab_prob(model) == approx(1.0, .00000001)
        
def test_perplexity() :
    assert perplexity(model, test_text) == approx(24979.5, .1)
    
def test_decompress() :
    decompressor = Decompressor(training_vocab)
    assert compress_decompress_accuracy(decompressor, model, test_text) > .79
   
    
