'''
Created on Oct 5, 2015

@author: tvandrun
'''

import sys
import operator


# Return the cost of the minimum-cost mutation (that is,
# the minimum edit distance) from source to target,
# based on the given costs for insertion, deletion, substitution,
# flip (transposition), and nop.
def edit_distance(source, target, costs):
    assert len(costs) == 5
    a = source
    b = target
    n = len(source)
    m = len(target)
    C = costs
    D = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j == 0:
                D[i][j] = 0
            elif i == 0:
                D[i][j] = j*C[0]
            elif j == 0:
                D[i][j] = i*C[0]
            else:
                D[i][j] = min(C[0]+D[i-1][j], C[1]+D[i][j-1], C[2]+D[i-1][j-1], C[3]+D[i-2][j-2] if a[i-1] == b[j-2] and a[i-2] == b[j-1] else 1 << 30, D[i-1][j-1] if a[i-1] == b[j-1] else 1 << 30)                                                                                                    

    # If we wanted to know *how* a word is transformed along
    # the least cost route to another word (ie, what the individual
    # mutations were), we would need an "actions" (or something like
    # that) array running parallel to distances.

    # Populate table here

    
    return D[n][m]


