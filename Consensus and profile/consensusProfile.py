#!/usr/bin/python
"""
Consensus and Profile
Given: A collection of at most 10 DNA strings of equal length (at most 1kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus
strings exist, then you may return any one of them.)
"""
import numpy as np
from collections import Counter
f = open("rosalind_cons.txt", 'rb')
data = {}
seq_id = ""
for line in f:
  if line[0] == ">":
    seq_id = line.strip()[1:]
    continue

  data.setdefault(seq_id,"")
  data[seq_id] += line.strip()

M = []
for i in data:
  M.append(list(data[i]))


n = len(M[0])
m = len(M)

consensus = ""
count = 0
for i in range(n):
  col = Counter()
  for j in range(m):
    col.setdefault(M[j][i], 0)
    count += 1
    col[M[j][i]] += 1
  if len(col.most_common()) > 0:
    consensus += col.most_common()[0][0]
print (consensus) 