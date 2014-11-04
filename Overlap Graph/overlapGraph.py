#!/usr/bin/python
"""
Overlap Graphs
Given: A collection of DNA strings in FASTA format having total length at most 10kbp.
Return: The adjacency list corresponding to an overlapping graph of 3 (O3). You may return
edges in any order.
"""
import re

def get_sequence():
  f = open("rosalind_grph.txt", "rb")
  data = {}
  seq_id = ""
  for line in f:
    if line[0] == ">":
  	  seq_id = line.strip()[1:]
      continue
    data.setdefault(seq_id,"")
    data[seq_id] += line.strip()
  return data



def get_adjacents(data):
  edges = []
  ids = data.keys()
  for i in range(len(ids)):
    for j in range(len(ids)):
      id1 = ids[i]
      id2 = ids[j]
      if id1 != id2:
        if data[id1][:3] == data[id2][-3:]:
          edges.append((id2, id1))

  return list(set(edges))

data = get_sequence()
adjacents = get_adjacents(data)
for a in adjacents: print a[0], a[1]