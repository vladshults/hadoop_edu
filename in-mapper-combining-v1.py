#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

"""
(lastKey, sum) = (None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split(" ")
    if lastKey and lastKey != key:
        print(lastKey + '\t' + str(sum))
        (lastKey, sum) = (key, int(value))
    else:
        (lastKey, sum) = (key, sum + int(value))

if lastKey:
    print(lastKey + '\t' + str(sum))
"""

for line in sys.stdin:
    dct = {}
    for word in line.strip().split(" "):
        if word in dct.keys():
            dct[word] += 1
        else:
            dct[word] = 1
    for w, v in dct.items():
        print(w + '\t' + str(v))
