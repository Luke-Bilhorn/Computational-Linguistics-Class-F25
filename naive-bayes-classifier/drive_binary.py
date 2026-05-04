import numpy as np
import sys
from nbc import NBClassifier
from bow import texts_to_count_vector
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords

source_dir = 'movie_reviews' if '-L' in sys.argv else '/homes/tvandrun/Public/cs384/nbc/movie_reviews'

print('Reading data...')
(v, X_all) = texts_to_count_vector(source_dir, vocab_size=2000, stop_words=stopwords.words('english'))
print('done.')
Y_all = np.array([0.] * 1000 + [1.] * 1000)
X_train,  X_test, Y_train, Y_test = train_test_split(X_all, Y_all,
                                                     random_state = 42 if '-R' in sys.argv else None)

print('Training classifier...')
nbc = NBClassifier(X_train, Y_train, 2)
print('done.')

nbc.sanity_check()

print('Classifying training set...')
Y_results = nbc.classify(X_train)
print('done.')
accuracy = sum(Y_results == Y_train)/len(Y_train)
print('Accuracy ' + str(accuracy))

print('Classifying test set...')
Y_results = nbc.classify(X_test)
print('done.')
accuracy = sum(Y_results == Y_test)/len(Y_test)
print('Accuracy ' + str(accuracy))
