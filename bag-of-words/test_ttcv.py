from bow import texts_to_count_vector
import numpy as np

stop_words_a = ['the', 'an', 'a', 'of', 'to', 'in']
stop_words_b = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that',
                    'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he',
                    'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by',
                    'from', 'they', 'we', 'her', 'she', 'or', 'an', 'will',
                    'my', 'all', 'would', 'there', 'their', 'what', 'so']

def test_num_vectors() :
    (voc, cv) = texts_to_count_vector('proverbs')
    assert len(cv) == 31
    (voc, cv) = texts_to_count_vector('proverbs', vocab_size=100)
    assert len(cv) == 31
    (voc, cv) = texts_to_count_vector('proverbs', vocab_size=100, stop_words=stop_words_a)
    assert len(cv) == 31
    (voc, cv) = texts_to_count_vector('shakespeare')
    assert len(cv) == 16
    (voc, cv) = texts_to_count_vector('shakespeare', vocab_size=100)
    assert len(cv) == 16
    (voc, cv) = texts_to_count_vector('shakespeare', vocab_size=100, stop_words=stop_words_a)
    assert len(cv) == 16

def test_vec_size_limited() :
    (voc, cv) = texts_to_count_vector('proverbs', vocab_size=25)
    assert len(cv[0]) == 25
    (voc, cv) = texts_to_count_vector('proverbs', vocab_size=100)
    assert len(cv[0]) == 100
    (voc, cv) = texts_to_count_vector('proverbs', vocab_size=100, stop_words=stop_words_a)
    assert len(cv[0]) == 100
    (voc, cv) = texts_to_count_vector('shakespeare', vocab_size=10)
    assert len(cv[0]) == 10
    (voc, cv) = texts_to_count_vector('shakespeare', vocab_size=12)
    assert len(cv[0]) == 12
    (voc, cv) = texts_to_count_vector('shakespeare', vocab_size=100, stop_words=stop_words_a)
    assert len(cv[0]) == 100
  
def test_vec_size_unlimited() :
    (voc, cv) = texts_to_count_vector('proverbs')
    assert len(cv[0]) == 1973
    (voc, cv) = texts_to_count_vector('proverbs', stop_words=stop_words_a)
    assert len(cv[0]) == 1967
    (voc, cv) = texts_to_count_vector('proverbs', stop_words=stop_words_b)
    assert len(cv[0]) == 1934
    (voc, cv) = texts_to_count_vector('shakespeare')
    assert len(cv[0]) == 701
    (voc, cv) = texts_to_count_vector('shakespeare', stop_words=stop_words_a)
    assert len(cv[0]) == 695
    (voc, cv) = texts_to_count_vector('shakespeare', stop_words=stop_words_b)
    assert len(cv[0]) == 662
 
def test_vocab_list() :
    (v,c) = texts_to_count_vector('proverbs', vocab_size=10)
    assert len(v) == 10
    for w in ['the', 'a', 'of', 'and', 'is', 'to', 'will', 'but', 'his', 'in'] :
        assert w in v
    (v,c) = texts_to_count_vector('proverbs', vocab_size=10, stop_words=stop_words_b)
    for w in ['is', 'who', 'your', 'man', 'are', 'him', 'whoever', 'lord', 'wicked', 'heart'] :
        assert w in v

def test_word_row_no_stopwords() :
    (v,c) = texts_to_count_vector('shakespeare', vocab_size=10)
    assert (c[:,v.index('and')] == [3., 1., 6., 7., 2., 6., 3., 3., 4., 3., 1., 4., 1., 2., 2., 2.]).all()
    assert (c[:,v.index('of')] == [0., 2., 1., 3., 2., 4., 4., 3., 3., 5., 2., 1., 1., 0., 1., 1.]).all()

def test_word_row_stopwords() :
    (v,c) = texts_to_count_vector('shakespeare', vocab_size=10, stop_words=stop_words_b)
    assert (c[:,v.index('thou')] == [2., 6., 8., 1., 0., 1., 0., 0., 3., 6., 5., 0., 5., 2., 5., 3.]).all()
    assert (c[:,v.index('when')] == [0., 0., 1., 4., 1., 0., 2., 0., 3., 0., 1., 0., 0., 2., 0., 1.]).all()

def test_text_column_limited() :
    (v,c) = texts_to_count_vector('shakespeare', vocab_size=10)
    assert sum(c[0]) == 27
    assert sum(c[14]) == 21

def test_text_column_unlimited() :
    (v,c) = texts_to_count_vector('shakespeare')
    assert sum(c[0]) == 112
    assert sum(c[14]) == 115
