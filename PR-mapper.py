#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys
import re


def printDataFromLinkList(m):
    pr = m.split('\t')[1]
    llist = (re.sub('\W+', ' ', m.split('\t')[2])).strip().split(' ')
    n = len(llist)
    count = round((float(pr)/n), 3)
    for item in llist:
        print(item, '%(number).3f' % {"number": count}, "{}", sep='\t')


for line in sys.stdin:
    if line:
        l = line.strip()

    conns = re.sub('\t|\s+', '\t', l)
    print(conns)
    printDataFromLinkList(conns)
