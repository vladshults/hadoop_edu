#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys
import re


lastKey = None
mass = []


def printDataFromMass(m):
    d = 0.0
    for item in m:
        if item.split(' ')[2] == '{}':
            d = d + float(item.split(' ')[1])
        else:
            llist = item.split(' ')[2]

    print(item.split(' ')[0], '%(number).3f' % {"number": (d*0.9+0.02)}, llist, sep='\t')


for line in sys.stdin:
    if line:
        l = line.strip()

    conns = re.sub('\t|\s+', ' ', l)
    key = conns.split(' ')[0]

    if lastKey == None:
        lastKey = key

    if lastKey != key:
        printDataFromMass(mass)
        mass = []
        mass.append(conns)
        lastKey = key
    else:
        mass.append(conns)


printDataFromMass(mass)
