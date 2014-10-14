#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


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

print ("This is the original DNA strand: ", dna)
print ("This is the reversed DNA strand: ", r_dna)

print (end='\n')
#print dna