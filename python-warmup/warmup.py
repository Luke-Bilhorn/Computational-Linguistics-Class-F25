'''
Created on May 26, 2023

Starter code for warm-up assignment
CSCI 384, Wheaton College (IL)
'''
from collections import Counter

def bigram_freq(text) :
     return Counter([text[i]+text[i+1] for i in range(len(text) - 1)])
          
alphacap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_cipher(plaintext, key):
     return ''.join([alphacap[(alphacap.index(plaintext[i]) + key) % len(alphacap)] if plaintext[i] in alphacap else plaintext[i] for i in range(len(plaintext))])    

def crack_caesar(ciphertext):
     freq = Counter([(ciphertext[i] if ciphertext[i] in alphacap else '#') for i in range(len(ciphertext))])
     freq.pop('#')
     E = alphacap.index(max(freq, key=freq.get)) - 4
     return caesar_cipher(ciphertext, (-E)%len(alphacap))
    
def vowel_path(board):
     n = len(board)
     m = len(board[0])
     best = [[None for j in range(m)] for i in range(n)]

     for i in range(n):
          for j in range(m):
               val = 1 if board[i][j] in "aoeui" else 0.5 if board[i][j] == 'y' else 0
               if i == 0 and j == 0:
                    best[i][j] = val
               elif i == 0:
                    best[i][j] = best[i][j-1] + val
               elif j == 0:
                    best[i][j] = best[i-1][j] + val
               else:
                    best[i][j] = max(best[i][j-1], best[i-1][j]) + val

     return best[n-1][m-1]
