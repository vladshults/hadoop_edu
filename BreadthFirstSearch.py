#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys
import re


for line in sys.stdin:
    if line:
        l = line.strip()

    id = l.split('\t')[0]
    d = l.split('\t')[1]
    conns = (re.sub('\W+?', ' ', l.split('\t')[2])).split()

    #print(id, d, conns)
    if conns == []:
        print(l)
    else:
        print(l)
        for i in conns:
            if d == 'INF':
                print(i + '\t' + d + '\t' + '{}')
            else:
                print(i + '\t' + str(int(d)+1) + '\t' + '{}')
