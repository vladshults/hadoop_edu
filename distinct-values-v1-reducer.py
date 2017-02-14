#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

lastKey = None


for line in sys.stdin:
    key = line.strip().split("\t")[0]
    #print(key)
    if lastKey != key:
        print(key)
    lastKey = key
