#!/usr/bin/python3
# -*- encoding: utf-8 -*-


import sys
import re

cnt = "1"

for line in sys.stdin:
    key = line.strip().split(":")[0]
    val = (re.sub(r'\W+?', ' ', line.replace(key + ':', ''))).strip().split()
    for i in val:
       print(i + '#' + key + '\t' + cnt)
