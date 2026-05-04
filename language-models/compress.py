#!/usr/bin/python

'''
Created on Sep 18, 2013

@author: tvandrun
'''
import re
import nltk
from nltk.corpus import PlaintextCorpusReader
import sys
import numpy as np

# Based on a function in Bird et al pg 103
def compress_word(word):
    # ^[AEIOUaeiou]+ means "one or more vowel at the start"
    # [EAIOUaeiou]+$ means "one or more vowel at the end"
    # [^AEIOUaeiou] means "not a vowel"
    pieces = re.findall(r'^[AEIOUaeiou]+|[EAIOUaeiou]+$|[^AEIOUaeiou]', word)
    # join the things in that list together, separated by the empty string
    return ''.join(pieces)


class Decompressor :
    def __init__(self, vocab):
        self.vocab = vocab
        self.vocab_compressions = {}
        for w in vocab :
            compressed = compress_word(w)
            if w[:4] == 'stew' :
                print(w + ' ' + compressed)
            if compressed in self.vocab_compressions.keys() :
                self.vocab_compressions[compressed].append(w)
            else :
                self.vocab_compressions[compressed] = [w]

    def decompress(self, word, history, lang_model):
        if word in self.vocab_compressions.keys() :
            candidate_probs = [(ww, lang_model.p(ww, history))
                               for ww in self.vocab_compressions[word]]
            chosen_word = sorted(candidate_probs, key=lambda x : x[1], reverse=True)[0][0]
            return chosen_word
        else :
            return "?" + word + "?"

def compress_decompress_accuracy(decompressor, model, original_text, step_through=False, show_text=False):
    if show_text :
        print("Original text:")
        print(' '.join(original_text))
    compressed_text = [compress_word(word) for word in original_text]
    if show_text :
        print("Compressed text:")
        print(' '.join(compressed_text))
    recovered_text = []    
    for i in range(len(compressed_text)):
        recovered_word = decompressor.decompress(compressed_text[i], recovered_text, model)
        if step_through :
            print(original_text[i], compressed_text[i], recovered_word, original_text[i] == recovered_word)
        recovered_text.append(recovered_word)
    if show_text :
        print("Recovered text:")
        print(' '.join(recovered_text))
    return np.mean([original == recovered for (original, recovered) in zip(original_text, recovered_text)])



        




    




    
