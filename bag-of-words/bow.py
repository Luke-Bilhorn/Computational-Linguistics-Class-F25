import numpy as np
import os
import re

def texts_to_count_vector(dir_name, vocab_size=None, stop_words=[]) :
    all_texts = []
    files = os.listdir(dir_name)
    files.sort()
    for filename in files :
        if filename[-4:] == '.txt' :
            with open(dir_name + '/' + filename, 'r') as f:
                file_contents = f.read().lower()
                all_texts.append(re.findall(r'\b[a-z\']+\b', file_contents))



    #unique_evens = list({x for sub in list_of_lists for x in sub if x % 2 == 0})
    vocab = list({word for text in all_texts for word in text if not (word in stop_words)}) #word not in stop_words ???
    vocab = {word for text in all_texts for word in text if not (word in stop_words)} #word not in stop_words ???
    vocab_size = min(len(vocab), vocab_size if vocab_size is not None else float('inf'))


    
    #counts = [[0 for _ in range(len(vocab))] for _ in range(len(all_texts))]
    counts = np.zeros((len(all_texts), len(vocab))) #vocab_size))
    global_counts = dict.fromkeys(vocab, 0)

    for i in range(len(all_texts)):
        for j in range(len(all_texts[i])):
            if all_texts[i][j] not in stop_words:
                global_counts[all_texts[i][j]] += 1


    order = [k for k, v in sorted(global_counts.items(), key=lambda x: x[1], reverse=True)]


    print(len(all_texts))
    print(counts.shape)
    for i in range(len(all_texts)):
        for j in range(len(all_texts[i])):
            if all_texts[i][j] in order:
                counts[i][order.index(all_texts[i][j])] += 1



    return (order[:vocab_size], np.array(counts[:, :vocab_size]))


    #make counts table for whole thing
    #sort based on totals 
    #return slice




    #make a set of counts for the whole entire thing


    #a = 'red' in all_texts[0]
    #loop through and make a list of unique types that are not stop words





















    #for text in all_texts:
    #    print(text)
    #    print("\n")

    #pass
