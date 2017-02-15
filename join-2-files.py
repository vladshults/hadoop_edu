#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


dct = {}


for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if key in dct.keys():
        upd = line.strip().split('\t')[1]
        dct.update({line[0]: upd})
    else:
        upd = line.strip().split('\t')[1]
        dct.update({line[0]: upd})

        print(dct)
        #dct = {}

