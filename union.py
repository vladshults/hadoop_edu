#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


lastKey = None


for line in sys.stdin:
    key = line.strip().split()[0]
    if lastKey != key:
        print(key)
    lastKey = key
