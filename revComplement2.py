#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="chiyuyen"
__date__ ="$Sep 23, 2014 1:44:54 PM$"

if __name__ == "__main__":
    import re

f = open('rosalind_revc.txt', 'r')
dna = f.readline()
f.close()

sub = {           \
        'A':'T',  \
        'T':'A',  \
        'C':'G',  \
        'G':'C',  \
}

r_dna = ''

for base in dna[::-1]:
    try:
        base = sub[base]
    except KeyError:
        pass
    r_dna += base

print r_dna
#print dna