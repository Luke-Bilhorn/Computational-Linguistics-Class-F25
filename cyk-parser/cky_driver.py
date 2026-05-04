'''
Created on Oct 25, 2021

@author: tvandrun
'''

import sys
import os
from cky_parser import parse

msg = sys.argv[1]
msg_toks = msg.split()

syntax_trees = parse(msg_toks)

d = 0
for syn_tree in syntax_trees :
    print(str(syn_tree))
    file = open("tree" + str(d) + ".dot", 'w')
    file.write("digraph G {")
    file.write(syn_tree.get_tree())
    file.write("}")
    file.close()
    os.system("dot tree" + str(d) + ".dot -Tpng:cairo > tree" + str(d) + ".png")
    d += 1
    

