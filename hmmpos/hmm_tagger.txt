'''
Created on Sep 30, 2021

@author: tvandrun
'''

import math
import numpy as np

# Convert a probability to a log probability.
# This differs from math.log only in that it is defined for 0 -> -inf
def log_prob(p):
    assert p >= 0
    if p == 0 :
        return -float('inf')
    else :
        return math.log(p)

# The tagset
tagset = ['VERB', 'NOUN', 'PRON', 'ADJ', 'ADV', 'ADP', 
          'CONJ', 'DET', 'NUM', 'PRT', 'X', '.']

DEBUG = True

class HMMTagger :
    def __init__(self, training_tagged, vocab):
        # Keep the vocabulary, we use it in the sanity check
        self.vocab = vocab 

        # Class should have the following instance variables:
        #     transition_probs, such that self.transition_probs[x][y] gives
        #           the probability of transitioning from state x to state x
        #     emission_probs, such that self.emission_probs[x][w] gives the
        #           probability of emitting word w in state x
        self.transition_probs = {tag: {tag: 0.0 for tag in tagset} for tag in tagset}
        self.emission_probs = {tag: {word: 0.0 for word in vocab} for tag in tagset}

        for i in range(len(training_tagged) - 1):
            self.transition_probs[training_tagged[i][1]][training_tagged[i+1][1]] += 1 

        for tag in self.transition_probs:
            Sum = sum(self.transition_probs[tag].values())
            for tag2 in self.transition_probs[tag]:
                self.transition_probs[tag][tag2] /= Sum

        for i in range(len(training_tagged)):
            self.emission_probs[training_tagged[i][1]][training_tagged[i][0]] += 1 

        for tag in self.emission_probs:
            Sum = sum(self.emission_probs[tag].values())
            for word in self.emission_probs[tag]: 
                self.emission_probs[tag][word] /= Sum #self.emission_probs[tag][word] / Sum



        # --- Code for training the HMMTagger goes here ---


       
        
    # Check that for all x, transition_probs[x] and emission_probs[x] are
    # proper probability functions.
    def sanity_check(self):
        for x in tagset :
            if DEBUG :
                print(x, sum([self.transition_probs[x][y] for y in tagset]))
            assert abs(1- sum([self.transition_probs[x][y] for y in tagset])) < .00001
            if DEBUG :
                print(x, sum([self.emission_probs[x][w] for w in self.vocab]))
            assert abs(1 - sum([self.emission_probs[x][w] for w in self.vocab])) < .00001
        print("Sanity check passed (transition and emission probabilities are valid)")
            
    # Tag a given text for parts of speech. Parameter text is a list of
    # strings representing the text. Return a list of string-tag pairs.
    def pos_tag(self, text):
         #return [(w, 'X') for w in text]  # delete this
         # Code for tagging text goes here

        N = len(tagset)
        M = len(text)
        O = text
        a = self.transition_probs
        b = self.emission_probs
        d = [[0 for i in range(N)] for t in range(M)]
        ps = [[None for i in range(N)] for t in range(M)]

        for t in range(M):
            for i in range(N):
                if t == 0:
                    d[t][i] = log_prob(b[tagset[i]][O[0]])
                else:
                    d[t][i] = max([d[t-1][j] + log_prob(a[tagset[j]][tagset[i]]) for j in range(N)]) + log_prob(b[tagset[i]][O[t]])

        for t in range(M):
            for i in range(N):
                if t == 0:
                    ps[t][i] = None
                else:
                    ps[t][i] = np.argmax([d[t-1][j] + log_prob(a[tagset[j]][tagset[i]]) for j in range(N)])

        I = int(np.argmax([d[M-1][i] for i in range(N)])) #wrapped in int?
        seq = [0 for t in range(M)]
        seq[M-1] = I #ps[M-1][I]
        for t in range(M-2, 0, -1):
            seq[t] = ps[t+1][seq[t+1]]
        return [(text[t], tagset[seq[t]]) for t in range(M)]