import numpy as np

import nltk
nltk.download('stopwords')


class NBClassifier :

    # Train this classifier
    #   X - Matrix of training data
    #   Y - Array of training targets
    #   num_classes - the number of classes; the integers in [0, num_classes) serve
    #                 as class labels
    def __init__(self, X, Y, num_classes):
        (N, self.D) = X.shape
        self.C = num_classes
        assert N == len(Y)
        assert all(y.is_integer() and 0 <= y and y < num_classes for y in Y)

        Y = np.array(Y).astype(int)
        class_counts = np.bincount(Y, minlength = int(self.C))[:int(self.C)]
        self.log_priors = np.log2(class_counts/N)#self.C)

        self.word_log_likelihoods = [[0 for j in range(self.D)] for i in range(self.C)]#N)]
        # Add training code here

        #bigdoc = [np.sum([X[i] for i in range(N) if Y[i] == c], axis=0) for c in range(self.C)]
        bigdoc = np.array([np.sum(X[Y == c], axis=0) for c in range(self.C)])

        #bigdoc = np.array(bigdoc)  # shape (C, D)
        denominators = np.sum(bigdoc + 1, axis=1, keepdims=True)  # shape (C, 1)
        self.word_log_likelihoods = np.log2((bigdoc + 1) / denominators)
        #self.word_log_likelihoods = np.log2((np.array(bigdoc) + 1)/np.array([sum([bigdoc[c, w] + 1 for w in range(self.D)]) for c in range(self.C)]))






#        function TRAIN NAIVE BAYES(D, C) returns V, log P(c), log P(w|c)
#for each class c ∈ C # Calculate P(c) terms
#Ndoc = number of documents in D
        #D
#Nc = number of documents from D in class c
        #DC = 
#logprior[c] ← log Nc
#Ndoc
#V ← vocabulary of D
#bigdoc[c] ← append(d) for d ∈ D with class c
#for each word w in V # Calculate P(w|c) terms
#count(w,c) ← # of occurrences of w in bigdoc[c]
#loglikelihood[w,c] ← log count(w, c) + 1
#∑
#w′ in V (count (w′, c) + 1)
#return logprior, loglikelihood, V
#function TEST NAIVE BAYES(testdoc, logprior, loglikelihood, C, V) returns best c
#for each class c ∈ C
#sum[c] ← logprior[c]
#for each position i in testdoc
#word ← testdoc[i]
#if word ∈ V
#sum[c] ← sum[c]+ loglikelihood[word,c]
#return argmaxc sum[c]
                                        
                                        
    def sanity_check(self):
        assert self.word_log_likelihoods.shape == (self.C, self.D)
        assert all(np.abs(1. - np.sum(2**self.word_log_likelihoods, axis=1)) < .0001)
        assert self.log_priors.shape == (self.C, )
    
    # Classify all vectors in an matrix of testing data. 
    #   X - A two-dim numpy array
    #   Return a numpy array of computed targets
    def classify(self, X):
        return np.array([self.classify_one(x) for x in X])
    
    # Classify one data point
    #   x - a numpy array representing a single data point
    #   Return the class computed for the given data point
    def classify_one(self, x):

        #print(x)
        #print('\n')
        sums = np.zeros(self.C)
        for c in range(self.C):
            sums[c] = self.log_priors[c]
            for i in range(len(x)):
                #if x[0][i] in x[1]:
                sums[c] += x[i] * self.word_log_likelihoods[c][i]
        return np.argmax(sums)



        #return np.argmax([c for c in range(self.C)])





        return None
