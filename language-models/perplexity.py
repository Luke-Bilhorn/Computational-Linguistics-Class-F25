'''
Created on Jul 11, 2023

@author: thomasvandrunen
'''

from langmod import *

infinity = float('inf')

def vocab_prob(model):
    vocab_probs = [model.p("NUM", []), model.p("OOV", []), model.p("PNCT", [])]
    for w in vocab :
        vocab_probs.append(model.p(w, []))
    vocab_probs.sort()
    return sum(vocab_probs)

def perplexity(model, test_text):
    total_log_prob = 0 
    history = []
    for w in test_text :
        prob = model.p(w, history)
        if prob == 0 :
            log_prob = infinity
        else :
            log_prob = math.log(prob) 
        total_log_prob += log_prob
        history.append(w)
    if total_log_prob != infinity :
        return math.exp(-total_log_prob/len(test_text))
    else :
        return infinity
        
