#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys
import re

lastKey = None
cnt = []

def processOfMassiv(v):
    l1 = []
    l2 = []
    for s in v:
        if s.split(':')[0] == 'query':
            l1.append(s.split(':')[1])
        if s.split(':')[0] == 'url':
            l2.append(s.split(':')[1])

    double_m = (l1, l2)
    return double_m

def printNameData(k, v):
    m, n = processOfMassiv(v)
    if len(m) == len(n):
            for i in range(0, len(m)):
                for j in range(0, len(m)):
                    print(k + '\t' + m[i] + '\t' + n[j])


for line in sys.stdin:
    key = re.split('\t|\s|\s{2}|\s{3}', line.strip())[0]
    val = line.replace(key, '').strip()
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
for k, v in sorted(dct.items()):
    l1 = []
    l2 = []
    list = v.split(';')

    for s in list:
        if s.split(':')[0] == 'query':
            l1.append(s.split(':')[1])
        if s.split(':')[0] == 'url':
            l2.append(s.split(':')[1])

        if len(l1) == len(l2):
            for i in range(0, len(l1)):
                for j in range(0, len(l1)):
                    print(k + '\t' + l1[i] + '\t' + l2[j])

#https://stepik.org/lesson/%D0%A0%D0%B5%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-17732/step/9?course=Hadoop-%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8-%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B8%D1%85-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BC%D0%BE%D0%B2-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85&discussion=342304
"""
