#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


dct = {}


for line in sys.stdin:
    for word in line.strip().split(" "):
        if word in dct.keys():
            dct[word] += 1
        else:
            dct[word] = 1


for w, v in dct.items():
    print(w + '\t' + str(v))
