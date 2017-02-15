#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


dct = {}


for line in sys.stdin:
    li = line.strip().split()
    if li[0] in dct.keys():
        upd = dct.get(li[0]) + li[1]
        dct.update({li[0]: upd})
    else:
        dct[li[0]] = li[1]

d = sorted(dct.keys())

for k in d:
    if len(dct.get(k)) == 1:
        print(k)

#my_dict.update({'another_key': 'yet_another_value'})  # Обновляем.
