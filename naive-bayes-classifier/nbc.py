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
        self.log_priors = np.log2(class_counts/N)

        self.word_log_likelihoods = [[0 for j in range(self.D)] for i in range(self.C)]
        bigdoc = np.array([np.sum(X[Y == c], axis=0) for c in range(self.C)])
        denominators = np.sum(bigdoc + 1, axis=1, keepdims=True)
        self.word_log_likelihoods = np.log2((bigdoc + 1) / denominators)
          
                                        
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
        sums = np.zeros(self.C)
        for c in range(self.C):
            sums[c] = self.log_priors[c]
            for i in range(len(x)):
                sums[c] += x[i] * self.word_log_likelihoods[c][i]
        return np.argmax(sums)