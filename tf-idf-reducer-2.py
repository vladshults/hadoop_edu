#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

lastKey = None
cnt = []


def printNameData(k, v):
    for i in v:
        print(k + "#" + i.split(';')[0] + '\t' + i.split(';')[1] + '\t' + str(len(v)))


for line in sys.stdin:
    key = line.strip().split("\t")[0]
    val = line.strip().split("\t")[1]
    if lastKey != key:
        if lastKey != None:
            printNameData(lastKey, cnt)
            cnt = []
            cnt.append(val)
            lastKey = key
        else:
            cnt.append(val)
            lastKey = key
    else:
        cnt.append(val)

printNameData(lastKey, cnt)


"""
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
