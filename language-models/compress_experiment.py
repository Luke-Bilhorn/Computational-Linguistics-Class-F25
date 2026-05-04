'''
Created on Aug 5, 2021

@author: thomasvandrunen
'''

from compress import compress_word, Decompressor, compress_decompress_accuracy
from langmod import *
import re
import numpy as np
import sys
from lm_train import lm_data, corpus_path, training_vocab, held_out_text



source_file_name = corpus_path + "test-smallish.txt"
source_file_raw_words = re.findall(r'[a-z][a-z\']*|\d+|[!$%*()\-:;\"\',.?]', open(source_file_name).read().lower())
source_text = [transform(w) for w in source_file_raw_words]
compressed_text = [compress_word(word) for word in source_text]

assert len(source_text) == len(compressed_text)

decompressor = Decompressor(training_vocab)

# Given language models

models = [ConstantLanguageModel(),    
          UnigramLanguageModel(lm_data), 
          UnigramLaplaceLanguageModel(lm_data),
          BigramLanguageModel(lm_data), 
          BigramLaplaceLanguageModel(lm_data), 
          TrigramLanguageModel(lm_data),
          TrigramLaplaceLanguageModel(lm_data),
          KatzCutOffGoodTuringLanguageModel(lm_data, 5)]
models.append(InterpolatedLanguageModel([models[1], models[2], models[3], models[4], models[5], models[6], models[7]],held_out_text))

# Then try interpolating among combinations of models 0-7

# models.append(??, ??, ??, ..., held_out_text)



for model in models :
    print("==%s==" % model.kind_of_model())
    acc = compress_decompress_accuracy(decompressor, model, source_text, step_through=(len(sys.argv) > 1 and sys.argv[1] == '-v'))
    print("Accuracy: " + str(acc * 100) + "%")


