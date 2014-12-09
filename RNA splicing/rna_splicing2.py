#!/usr/bin/env python
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

handle = open("D:/python/dataset/rosalind_splc.txt", "r")
lines = list(SeqIO.parse(handle, "fasta"))
chain = lines[0]
lines = lines[1:]

#Determine where the introns are
introns = []
for line in lines :
    start = chain.seq.find(line.seq)
    if(start > 0) :
        introns.append([start,start + len(line.seq)-1])
        print("Intron %s has been detected in %i position" % (line.seq, start+1))
introns.append([start,start + len(line.seq)-1])
introns.sort()

last_start=0
ORF = Seq("",generic_dna)
#Add the exons to the ORF
for intron in introns :
    ORF += chain[last_start:intron[0]]
    last_start = intron[1]+1
ORF += chain[last_start:]
print(ORF.seq.translate())