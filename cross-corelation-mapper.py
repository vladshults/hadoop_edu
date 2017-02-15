#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


for line in sys.stdin:
    li = line.strip().split(" ")
    for i in range(0, len(li)):
        for j in range(0, len(li)):
            if li[i] != li[j]:
                print(li[i] + ',' + li[j] + '\t' + '1')
