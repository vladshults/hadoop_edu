#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

cnt = "1"

for line in sys.stdin:
    k = line.strip().split("\t")[0]
    v = line.strip().split("\t")[1].split(",")
    for i in v:
       print(k + ',' + i + "\t" + cnt)


"""
    dct = {}

    for line in sys.stdin:
        for word in line.strip().split(" "):
            if word in dct.keys():
                dct[word] += 1
            else:
                dct[word] = 1

    for w, v in dct.items():
        print(w + '\t' + str(v))
"""
