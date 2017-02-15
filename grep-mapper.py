#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


pattern = '\tuser10\t'


for line in sys.stdin:
    li = line.strip()
    if li.find(pattern) != -1:
        print(li)
