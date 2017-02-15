#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

(lastKey, name) = (None, None)
s = set()

for line in sys.stdin:
    (key, value) = line.strip().split()
    if lastKey == key and name != value:
        s.add(lastKey)
    lastKey = key

for i in sorted(s):
    print(i)
