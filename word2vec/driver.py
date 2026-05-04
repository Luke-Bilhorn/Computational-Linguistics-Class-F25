from word2vec import word2vec
import sys
import numpy as np
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')

def cos_sim(a, b):
    return np.dot(a, b)/(np.linalg.norm(a, ord=2)*np.linalg.norm(b, ord=2))

def dist_sim(a, b) :
    return np.linalg.norm(a-b)

filename = sys.argv[1]
(vocab, embeddings) = word2vec(filename, trace=True, epochs=500)

num_types = len(vocab)

assert embeddings.shape == (num_types, 50)

print("Finding similarities between pairs...")
pair_similarities = []
for i in range(num_types) :
    if vocab[i] not in stopwords.words('english') :
        for j in range(i+1, num_types) :
            if vocab[j] not in stopwords.words('english') :
                pair_similarities.append((vocab[i], vocab[j], dist_sim(embeddings[i], embeddings[j])))

print("Sorting pairs by similarity...")
pair_similarities.sort(key=lambda x: x[2])


print("Most similar:")
for i in range(100) :
    print(pair_similarities[i])


