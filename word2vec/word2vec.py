import nltk
import numpy as np
from random import random


# --- Vector distance measures ---

# Compute the cosine of the angle between two vectors
def cos_sim(a, b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

# Compute the Euclidean distance between two vectors
def dist_sim(a, b) :
    return np.linalg.norm(a-b)

# --- Other useful functions ---

# Return a list of the indicies in a window of size k around index i,
# with maximum index n    
def window(i, k, n) :
    return [j for j in range(i-k, i+k+1) if j >=0 and j != i and j < n]

# Compute the logistic (sigmoid) function
def logistic(x) :
    return 1 / (1 + np.exp(-x))

# Compute the logistic applied to the dot product of two vectors,
# that is sigma(a dot b)
def log_dot(a, b) :
    return logistic(np.dot(a, b))

# Compute the cross-entropy (negative log likelihood) loss 
# for a given data point, given the 
def loss_ce(target, context_pos, context_negs, W, C) :
    w = W[target]
    c_pos = C[context_pos]
    c_negs = [C[i] for i in context_negs]
    return - (np.log2(log_dot(c_pos, w)) + 
              sum([np.log2(log_dot(-c_neg, w)) for c_neg in c_negs]))

# -- Helper functions for the word2vec training algorithm --

# Pick a random noise word from a set, given a probability function.
# (Actually this function does not depend on noise words or
#  anything else about word2vec---it just picks a random
#  element from a list based on a probability function.)
def pick_noise_word(noise_words, wpf) :
    nonce = random()
    running = 0.0
    i = 0
    last_i = len(noise_words) - 1
    while i < last_i and running < nonce : 
        running += wpf(noise_words[i])
        i += 1
    return i

# Compute a list of positive training samples from a sequence of tokens
# tokens: The text as a sequence of tokens, which are actually word ids, 
#         not strings
# context_words: A list of sets for mapping each word type to its set
#         of context words, initially with each type mapped to an empty set
# L: The size of the window for finding context words
# Return a list of (target, positive-context) pairs of words (as indices)
# Postcondition: For each word type w, context_words[w] is the set of all context
# words found for type w 
def find_positive_training_samples(tokens, context_words, L):
    n = len(tokens)
    ret = []
    for i in range(n):
        for j in range(-L, L + 1):
            if j != 0 and i + j >= 0 and i + j < n:
                ret.append((tokens[i], tokens[i + j]))
                context_words[tokens[i]].add(tokens[i + j])
    return ret

# Update the target and context weights for one training sample. All word
# parameters are represented as indices.
# target: The target word of this training sample
# context_pos: The positive context word for this training sample
# context_negs: The list of negative context words for this training sample
# W: The matrix of target word vectors
# C: The matrix of context word vectors
# eta: The learning rate
def update_weights_one_sample(target, context_pos, context_negs, W, C, eta):
    h = eta

    #check out copies of these variables
    w = np.copy(W[target])
    cpos = np.copy(C[context_pos])
    cneg = [np.copy(C[context_negs[i]]) for i in range(len(context_negs))]

    #edit the copies of these variables
    cpos -= h*(logistic(np.dot(C[context_pos], w)) - 1)*W[target]
    cneg = [C[context_negs[i]] - h*logistic(np.dot(C[context_negs[i]], W[target]))*W[target] for i in range(len(context_negs))]
    w -= h*((logistic(np.dot(C[context_pos], W[target])) - 1)*C[context_pos] + sum([logistic(np.dot(C[context_negs[i]], W[target]))*cneg[i] for i in range(len(context_negs))]))

    #return variable copies
    for i in range(len(context_negs)):
        C[context_negs[i]] = np.copy(cneg[i])
    C[context_pos] = np.copy(cpos)
    W[target] = np.copy(w)

# Compute a matrix of word embeddings from a corpus
# filename: The string name of the file containing the corpus
# D: The desired size of the embeddings
# L: The window size for finding context words
# alpha: The weight for the weighted probability function
# eta: The learning rate
# epochs: The number of passes of stochastic gradient descent over the training data
# trace: A flag to control output tracing the phases of the algorithm
def word2vec(filename, D=50, L=2, k=2, alpha=.75, eta=.001, epochs=10, trace=False) :
    # Load and tokenize the file; compute the frequency distribution and 
    if trace :
        print("Loading file...")
    tokens = [x.lower() for x in nltk.word_tokenize(open(filename).read()) if x.isalpha()]
    n = len(tokens)

    if trace :
        print("Counting words...")
    total_counts = nltk.FreqDist(tokens)
    vocab = list(set(tokens))
    V = len(vocab)
    inverse_vocab = {vocab[i]:i for i in range(V)}
    # Convert the tokens from strings to integer ids
    tokens = [inverse_vocab[w] for w in tokens]
    

    # make weighted probability function
    wpf_denom = sum([total_counts[w]**alpha for w in vocab])
    wpf = lambda w: total_counts[w]**alpha / wpf_denom

    # find training samples
    if trace:
        print("Finding positive training samples...")
    context_words = [set() for v in range(V)]
    pos_training_samples = find_positive_training_samples(tokens, context_words, L) 

    if trace:
        print("Finding negative training samples...")
    training_samples = [(w, c, [pick_noise_word(list(set(vocab)-context_words[w]), wpf) for x in range(k)]) 
                        for (w,c) in pos_training_samples]

    num_samples = len(training_samples) * (k+1)
 
    # make initial vectors
    W = np.random.rand(V, D)  # target
    C = np.random.rand(V, D)  # context

    loss_history = []  # Used to trace the loss across epochs
    
    if trace :
        print("Training embeddings...")
    ep = 0 # epochs so far
    while ep < epochs :
        if trace and ep % 25 == 0:
            print("Epoch " + str(ep))
        for (target, context_pos, context_negs)  in training_samples :
            update_weights_one_sample(target, context_pos, context_negs, W, C, eta)
    
        loss_history.append(sum([loss_ce(target, context_pos, context_negs, W, C) 
                                 for (target, context_pos, context_negs) in training_samples])/num_samples)
        if trace :
            print("Loss: " + str(loss_history[-1]))
        ep += 1
         
    if trace :
        print("Word2Vec finished")                          

    min_loss = min(loss_history)
    min_loss_epoch = loss_history.index(min_loss)
    if trace :
        print("Minimum loss " + str(min_loss) + " at epoch " + str(min_loss_epoch))

    return (vocab, W + C)


     
