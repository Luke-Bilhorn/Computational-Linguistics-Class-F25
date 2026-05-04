'''
Created on Jul 11, 2023

@author: thomasvandrunen
'''

from compress import compress_word, Decompressor, compress_decompress_accuracy
from langmod import *
import re
import numpy as np
import sys
from lm_train import lm_data, corpus_path, training_vocab

source_file_name = corpus_path + sys.argv[1]
source_file_raw_words = re.findall(r'[a-z][a-z\']*|\d+|[!$%*()\-:;\"\',.?]', open(source_file_name).read().lower())
source_text = [transform(w) for w in source_file_raw_words]
compressed_text = [compress_word(word) for word in source_text]

assert len(source_text) == len(compressed_text)

decompressor = Decompressor(training_vocab)


model = eval(sys.argv[2])
acc = compress_decompress_accuracy(decompressor, model, source_text, show_text=True)
print("Accuracy: " + str(acc * 100) + "%")


