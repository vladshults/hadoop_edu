#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys


for line in sys.stdin:
    li = line.strip().split(" ")
    for i in range(0, len(li)):
        dct = {}
        for j in range(0, len(li)):
            if li[i] != li[j]:
                if li[j] in dct.keys():
                    dct[li[j]] = dct.get(li[j]) + 1
                else:
                    dct[li[j]] = 1
        str = ",".join(["%s:%s" % (k, v) for k, v in sorted(dct.items())])
        print(li[i] + '\t' + str)
