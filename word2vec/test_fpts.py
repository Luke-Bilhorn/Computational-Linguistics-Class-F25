'''
Created on Nov 14, 2023

@author: tvandrun
'''

from word2vec import find_positive_training_samples

text1 = "that's just my lunch that don't mean nothing"
text2 = 'Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do Once or twice she had peeped into the book her sister was reading but it had no pictures or conversations in it and what is the use of a book thought Alice without pictures or conversations'

def run_text1() :
    tokens = text1.split()
    vocab = tokens
    tokens = [vocab.index(w) for w in tokens]
    context_words = [set() for i in range(len(vocab))]
    return (vocab, context_words, 
            find_positive_training_samples(tokens, context_words, 2))

def run_text2() :
    tokens = text2.split()
    vocab = tokens
    tokens = [vocab.index(w) for w in tokens]
    context_words = [set() for i in range(len(vocab))]
    return (vocab, context_words, 
            find_positive_training_samples(tokens, context_words, 3))

def test_short_context_words():
    (vocab, cw, pts) = run_text1()
    assert len(pts) == 26
    i = lambda w : vocab.index(w)
    assert (i('lunch'), i('my')) in pts
    assert (i("don't"), i('nothing')) in pts
    assert (i('that'), i('nothing')) not in pts
    
def test_short_vocab() :
    (vocab, cw, pts) = run_text1()
    i = lambda w : vocab.index(w)
    assert cw[i('just')] == {i("that's"), i('my'),i('lunch')}
    assert len(cw[i('that')]) == 4
    assert len(cw[i('nothing')]) == 2
    assert len(cw[i('mean')]) == 3
    
def test_longer_context_words() :
    (vocab, cw, pts) = run_text2()
    assert len(pts) == len(text2.split()) * 6 - 12
    i = lambda w : vocab.index(w)
    assert (i('sister'), i('bank')) in pts
    assert (i("sister"), i('reading')) in pts
    assert (i('very'), i('was')) not in pts

def test_longer_vocab() :
    (vocab, cw, pts) = run_text2()
    i = lambda w : vocab.index(w)
    assert cw[i('tired')] == {i('to'),i('get'),i('very'),i('of'),i('sitting'),i('by')}