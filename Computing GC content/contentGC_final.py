from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.SeqUtils import GC
from operator import itemgetter, attrgetter, methodcaller

high_id = None
high_gc = 0

for record in SeqIO.parse("dataset/rosalind_gc.fasta", "fasta", generic_dna):

	#print(record)
    gc = GC(record.seq)
    if gc > high_gc:
       high_id = record.id
       high_gc = gc
       #print(gc)


print(high_id)
print('{:.3f}'.format(high_gc))	