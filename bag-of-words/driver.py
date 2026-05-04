from bow import texts_to_count_vector

stop_words_a = ['the', 'an', 'a', 'of', 'to', 'in']
stop_words_b = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that',
                    'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he',
                    'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by',
                    'from', 'they', 'we', 'her', 'she', 'or', 'an', 'will'
                    'my', 'all', 'would', 'there', 'their', 'what', 'so']


(v,c) = texts_to_count_vector('shakespeare', vocab_size=10)
print(v)
print(c[:,0])
print(c[:,5])
print(c[:,v.index('and')])
(v,c) = texts_to_count_vector('shakespeare', vocab_size=10, stop_words=stop_words_b)
print(v)
print(c[:,0])
print(c[:,6])

