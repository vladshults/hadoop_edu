#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


pattern = 'http'


for line in sys.stdin:
    li = line.strip().split()
    for l in li:
        if l.find(pattern) != -1:
            print(l)
