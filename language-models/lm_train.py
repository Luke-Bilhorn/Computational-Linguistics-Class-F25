'''
Created on Jul 12, 2023

@author: thomasvandrunen
'''

from langmod import LanguageModelData, transform

import re

corpus_path = "/homes/tvandrun/Public/cs384/langmod_texts/"

training_file_name = corpus_path + "training.txt"
training_raw_words = re.findall(r'[a-z][a-z\']*|\d+|[!$%*()\-:;\"\',.?]', open(training_file_name).read().lower())
training_text = [transform(w) for w in training_raw_words]
training_vocab = set(training_text)

held_out_file_name = corpus_path + "heldout-small.txt"
held_out_raw_words = re.findall(r'[a-z][a-z\']*|\d+|[!$%*()\-:;\"\',.?]', open(held_out_file_name).read().lower())
held_out_text = [transform(w) for w in held_out_raw_words]

lm_data = LanguageModelData(training_text)
