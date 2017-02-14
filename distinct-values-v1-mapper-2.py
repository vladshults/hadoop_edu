#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys

cnt = "1"

for line in sys.stdin:
    k = line.strip().split(",")[1]
    print(k + '\t' + cnt)
