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


models = [ConstantLanguageModel(),    
          UnigramLanguageModel(lm_data), 
          UnigramLaplaceLanguageModel(lm_data),
          BigramLanguageModel(lm_data), 
          BigramLaplaceLanguageModel(lm_data), 
          TrigramLanguageModel(lm_data)]


def test_vocab() :
    for m in models :
        assert vocab_prob(m) == approx(1.0, .00000001)
        
def test_perplexity() :
    assert perplexity(models[0], test_text) == approx(61338.0, .1)
    assert perplexity(models[2], test_text) == approx(572.3, .1)
    assert perplexity(models[4], test_text) == approx(3735.4, .1)
    
def test_decompress() :
    decompressor = Decompressor(training_vocab)
    expected_accuracies = [.72, .92, .92, .89, .90, .81]
    for (model, acc) in zip(models, expected_accuracies) : 
        assert compress_decompress_accuracy(decompressor, model, test_text) > acc
   
    
