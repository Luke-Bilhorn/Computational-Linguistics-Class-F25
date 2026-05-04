#!/usr/bin/python
'''
Created on Sep 18, 2013

@author: tvandrun
'''

from nltk import FreqDist
from collections import Counter
import re
import math


# The set of characters that can appear in a token. Note that 
# an apostrophe counts as a letter.
alphabet = "abcdefghijklmnopqrstuvwxyz'"

# The vocabulary (set of tokens)
vocab = set(w.lower() for w in open("vocab").read().splitlines() if all(c in alphabet for c in w))


# Transform a raw token into a token in the vocabulary. There
# are three special tokens respectively indicating a number, an
# "out of vocabulary" words, and a punctuation.
def transform(w):
    if w.isdigit():
        return "NUM"    
    elif all(c in alphabet for c in w) :
        if w in vocab :
            return w
        else :
            return "OOV"
    else :
        return  "PNCT"


# The size of the vocabulary.
# The "+ 3" is for NUM, OOV, and PNCT, which are treated as vocabulary
# words but are not in the set vocab
V = len(vocab) + 3



# Class representing information processed from a training text
# that can be used by a language model. 
class LanguageModelData:
    
    def __init__(self, text):
        self.fd_unigrams = FreqDist(text)
        self.fd_bigrams = FreqDist([tuple(text[i:i+2]) for i in range(len(text) - 1)])
        self.fd_trigrams = FreqDist([tuple(text[i:i+3]) for i in range(len(text) - 2)])
        # Number of tokens in the text
        self.N = len(text)
        # Count of counts or frequency of frequencies, used b Good-Turing
        self.count_of_counts = FreqDist([self.fd_unigrams[w] for w in vocab.union(["NUM", "OOV", "PNCT"])])

    def unigram_count(self, w):
        return float(self.fd_unigrams[w])
    
    def bigram_count(self, w1, w2):
        return float(self.fd_bigrams[(w1, w2)])
        
    def trigram_count(self, w1, w2, w3):
        return float(self.fd_trigrams[(w1, w2, w3)])



# ----- Provided language models -----

class ConstantLanguageModel :
    
    def p(self, w, h):
        return 1 / float(V)
    
    def kind_of_model(self):
        return "constant"

class UnigramLanguageModel :
    
    def __init__(self, lm_data):
        self.lm_data = lm_data
        
    def p(self, w, h):
        return float(self.lm_data.fd_unigrams[w]) / self.lm_data.N
    
    def kind_of_model(self):
        return "unigram"

class UnigramLaplaceLanguageModel :
    
    def __init__(self, lm_data):
        self.lm_data = lm_data
        
    def p(self, w, h):
        return float(self.lm_data.fd_unigrams[w] + 1) / (self.lm_data.N + V)
    
    def kind_of_model(self):
        return "unigram with laplace smoothing"
    
class BigramLanguageModel :
    
    def __init__(self, lm_data):
        self.lm_data = lm_data
        
    def p(self, w, h):
        try :
            if len(h) == 0 :
                return float(self.lm_data.fd_unigrams[w]) / self.lm_data.N
            else :
                return float(self.lm_data.fd_bigrams[(h[-1], w)]) / self.lm_data.fd_unigrams[h[-1]]
        except ZeroDivisionError :
            return 0.0

    def kind_of_model(self):
        return "bigram"
        
class BigramLaplaceLanguageModel :
    
    def __init__(self, lm_data):
        self.lm_data = lm_data
        
    def p(self, w, h):
        if len(h) == 0 :
            return float(self.lm_data.fd_unigrams[w] + 1) / (self.lm_data.N + V)
        else :
            return float(self.lm_data.fd_bigrams[(h[-1], w)] + 1) / (self.lm_data.fd_unigrams[h[-1]] + V)
                
    def kind_of_model(self):
        return "bigram with Laplace smoothing"
        
        
class TrigramLanguageModel :
   
    def __init__(self, lm_data):
        self.lm_data = lm_data
        
    def p(self, w, h):
        try :
            if len(h) == 0 :
                return float(self.lm_data.fd_unigrams[w] + 1) / (self.lm_data.N + V)
            elif len(h) == 1 :
                return float(self.lm_data.fd_bigrams[(h[0], w)]) / self.lm_data.fd_unigrams[h[-1]]
            else :
                return float(self.lm_data.fd_trigrams[(h[-2], h[-1], w)]) / self.lm_data.fd_bigrams[(h[-2], h[-1])]
        except ZeroDivisionError :
            return 0.0

    def kind_of_model(self):
        return "trigram"

# ---------  Language models for you to finish -----------

class TrigramLaplaceLanguageModel :
    
    def __init__(self, lm_data):
        self.lm_data = lm_data
        
    def p(self, w, h):
        if len(h) == 0 :
            return float(self.lm_data.fd_unigrams[w] + 1) / (self.lm_data.N + V)
        elif len(h) == 1:
            return float(self.lm_data.fd_bigrams[(h[-1], w)] + 1) / (self.lm_data.fd_unigrams[h[-1]] + V)
        else :
            return float(self.lm_data.fd_trigrams[(h[-2], h[-1], w)] + 1) / (self.lm_data.fd_bigrams[(h[-2], h[-1])] + V)
                


    def kind_of_model(self):
        return "trigram with Laplace smoothing"
    

class KatzCutOffGoodTuringLanguageModel :
    
    def __init__(self, lm_data, k):
        self.lm_data = lm_data
        self.k = k

    def p(self, w, h):
        data = self.lm_data
        N = data.N
        k = self.k
        C = data.fd_unigrams

        n = data.count_of_counts
        r = C[w]

        if C[w] == 0:
            return n[1]/(N*n[0])
        elif C[w] <= k:
            return ((r+1)*n[r+1]/n[r]-r*(k+1)*n[k+1]/n[1])/(N*(1-(k+1)*n[k+1]/n[1]))
        else:
            return C[w]/N

    def kind_of_model(self):
        return "Katz-cut-off Good-Turing"


    
class InterpolatedLanguageModel :
    
    def __init__(self, lang_mods, held_out_text):
        self.lang_mods = lang_mods
        self.weights = [1.0 / len(lang_mods) for lm in lang_mods]

        #Lambda = self.weights
        P = lang_mods #j of this
        w = held_out_text #i of this
        k = len(lang_mods)
        M = len(w)
        I = M
        J = k

        z = [[0 for j in range(J)] for i in range(I)]

        ALLnew = 3.1415926535897932384 #for example
        ALLold = sum([math.log(self.p(w[i], w[:i])) for i in range(I)])/M
        while (True): #(abs(ALLold - ALLnew) > 0.01):
            #E step:
            for i in range(I):
                for j in range(J):
                    z[i][j] = self.weights[j]*P[j].p(w[i], w[:i])/sum([self.weights[jj]*P[jj].p(w[i], w[:i]) for jj in range(J)])

            #M step:
            self.weights = [sum([z[i][j] for i in range(I)])/M for j in range(J)]

            #Check for convergece:
            ALLold = ALLnew
            ALLnew = sum([math.log(self.p(w[i], w[:i])) for i in range(I)])/M
            if abs(ALLold - ALLnew) < 0.01:
                break

        # Train the weights using "degenerate" EM
        



    def p(self, w, h):
        return sum([weight * lang_mod.p(w, h) 
                   for weight, lang_mod in zip(self.weights, self.lang_mods)])

    def kind_of_model(self):
        return "Interpolated: %s"  % " + ".join(["%s*%s"% (weight, lang_mod.kind_of_model())  
                                                for (weight, lang_mod) in zip(self.weights, self.lang_mods)])
