#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


d = {}
ds = {}
l = []
numbers = []


for line in sys.stdin:
    l.append(line.strip())

ls = l[1:-1]
start = int(l[-1].split(' ')[0])
finish = int(l[-1].split(' ')[1])
for k in range(1, int(l[0].split(' ')[0])+1):
    if k != start:
        d[k] = float('inf')
    else:
        d[start] = 0


ds = d.copy()


def select_pair_with_min_distance():
    m = min(d.values())
    for k, v in d.items():
        if v == m:
            item = d.pop(k)
            return k, item


while d != {}:
    vertex = select_pair_with_min_distance()
    for vector in ls:
        if int(vector.split(' ')[0]) == vertex[0]:
            key = int(vector.split(' ')[1])
            dist = vertex[1] + int(vector.split(' ')[2])
            if ds.get(key) > dist:
                ds[key] =  dist
                d[key] =  dist


if ds[finish] == float('inf'):
    print(int(-1))
else:
    print(ds[finish])
