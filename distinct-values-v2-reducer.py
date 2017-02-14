#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

lst = []
dct = {}

for line in sys.stdin:
    count, word = line.strip().split("\t")
    ls = word + ';' + count
    lst.append(ls)

l = set(lst)

for lin in l:
    key = lin.split(";")[0]
    if key in dct.keys():
        dct[key] = dct.get(key) + 1
    else:
        dct[key] = 1

for w, v in dct.items():
    print(w + '\t' + str(v))
