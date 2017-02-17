#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

lastKey = None
cnt = 1

for line in sys.stdin:
    key = line.strip().split("\t")[0]
    if lastKey != key:
        if lastKey != None:
            print(lastKey.split('#')[0] + '\t' + lastKey.split('#')[1] + '\t' + str(cnt))
            cnt = 1
            lastKey = key
        else:
            lastKey = key
    else:
        cnt += 1

print(lastKey.split('#')[0] + '\t' + lastKey.split('#')[1] + '\t' + str(cnt))

"""
for line in sys.stdin:
    key = line.strip().split("\t")[0]
    #print(key)
    if lastKey != key:
        print(key)
    lastKey = key
"""