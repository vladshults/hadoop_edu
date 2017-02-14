#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


(lastKey, sum) = (None, 0)

n = 0

for line in sys.stdin:
    key = line.strip().split("\t")
    if lastKey and lastKey != key:
        print(lastKey + '\t' + str(int(sum/n)))
        (lastKey, sum) = (key, int(value))
        n = 1
    else:
        (lastKey, sum) = (key, sum + int(value))
        n += 1
if lastKey:
    print(lastKey + '\t' + str(int(sum/n)))