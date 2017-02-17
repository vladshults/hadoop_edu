#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

cnt = '1'

for line in sys.stdin:
    key = line.strip().split("\t")[0]
    docid = line.strip().split("\t")[1]
    count = line.strip().split("\t")[2]
    print(key + '\t' + docid + ';' + count + ';' + cnt)
