#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

(lastKey, sum) = (None, 0)

n = 0

for line in sys.stdin:
    (k, v) = line.strip().split("\t")
    (key, value) = (k, v.split(";")[0])
    if lastKey and lastKey != key:
        print(lastKey + '\t' + str(sum) + ";" + str(n))
        (lastKey, sum) = (key, int(value))
        n = 1
    else:
        (lastKey, sum) = (key, sum + int(value))
        n += 1
if lastKey:
    print(lastKey + '\t' + str(sum) + ";" + str(n))
