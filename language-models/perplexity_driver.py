'''
Created on Sep 30, 2015

@author: tvandrun
'''

from langmod import *
from perplexity import *
import re
import math
from lm_train import lm_data, corpus_path, training_vocab, held_out_text


test_file_name = corpus_path + "test-smallish.txt"


test_raw_words = re.findall(r'[a-z][a-z\']*|\d+|[!$%*()\-:;\"\',.?]', open(test_file_name).read().lower())
test_text = [transform(w) for w in test_raw_words]

# Given language models

models = [ConstantLanguageModel(),    
          UnigramLanguageModel(lm_data), 
          UnigramLaplaceLanguageModel(lm_data),
          BigramLanguageModel(lm_data), 
          BigramLaplaceLanguageModel(lm_data), 
          TrigramLanguageModel(lm_data)]


# Models you need to write. Uncomment these as you write them

# models.append(TrigramLaplaceLanguageModel(lm_data))
# models.append(KatzCutOffGoodTuringLanguageModel(lm_data, 5)) 
# models.append(InterpolatedLanguageModel([models[0],models[1]],held_out_text))

# Then try interpolating among combinations of models 0-7

# models.append(InterpolatedLanguageModel([??, ??, ??, ...], held_out_text)




infinity = float('inf')

for model in models :
    print("==%s==" % model.kind_of_model())

    print("total probability of vocab: ", vocab_prob(model))

    perplx = perplexity(model, test_text)
    if perplx != infinity :
        print("perplexity: %s" % perplx)
    else :
        print("infinite perplexity")
        
