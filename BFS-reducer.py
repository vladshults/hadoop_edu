#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys
import re


lastKey = None
mass = []


def printDataFromMass(m):
    k = m[0].split(' ')[0]
    dist = []
    vertexes = []
    for st in m:
        if st.split(' ')[1] == 'INF':
            d = float('inf')
        else:
            d = int(st.split(' ')[1])
        dist.append(d)
        vertexes.append(st.split(' ')[2])

    min_dist = min(dist)
    if min_dist == float('inf'):
        min_dist = 'INF'

    vert = '{}'

    for v in vertexes:
        if v != '{}':
            vert = v

    print(k + '\t' + str(min_dist) + '\t' + vert)


for line in sys.stdin:
    if line:
        l = line.strip()

    conns = re.sub('\t|\s+', ' ', l)
    key = conns.split(' ')[0]

    if lastKey == None:
        mass.append(conns)
        lastKey = key

    if lastKey != key:
        printDataFromMass(mass)
        mass = []
        mass.append(conns)
        lastKey = key
    else:
        mass.append(conns)


printDataFromMass(mass)
