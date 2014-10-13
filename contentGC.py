#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="chiyuyen"
__date__ ="$Sep 23, 2014 1:46:33 PM$"

if __name__ == "__main__":
    f = open('rosalind_gc.txt', 'r')
raw_samples = f.readlines()
f.close()

samples = {}
cur_key = ''

for elem in raw_samples:
    if elem[0] == '>':
        cur_key = elem[1:].rstrip()
        samples[cur_key] = ''
    #else:
     #   samples[cur_key] += elem.rstrip()

for s_id, s in samples.iteritems():
    samples[s_id] = (float(s.count('G') + s.count('C'))/len(s))*100

(s_id, gc) = max(list(samples.iteritems()), key = lambda item:item[1])
print s_id
print gc + '%'

