from Bio import SeqIO
from Bio import motifs
from Bio import Motif

#for record in SeqIO.parse("dataset/rosalind_gc.fasta", "fasta", generic_dna):


f = open('dataset/rosalind_subs.txt', 'r')
dnaSequence = f.readline()
f.close()

print (dnaSequence)

#from Bio.Seq import Seq 
#instances = [Seq("TACAA"),
#			 Seq("TACGC"),
#	         Seq("TACAC"),
#	         Seq("TACCC"),
#	         Seq("AACCC"),
#	         Seq("AATGC"),
#	         Seq("AATGC"),
#	         ]

#instances = [Seq("ATAT")]


#m = motifs.create(instances)

from Bio.Alphabet import IUPAC
m = Motif.Motif(alphabet=IUPAC.unambiguous_dna)
#This is for now just an empty container, so let’s add some sequences to our newly created motif:

from Bio.Seq import Seq
m.add_instance(Seq("GCCTCTCGC",m.alphabet))


#print (m)

###the position function start with 0 so to get exact position we need to add 1 to get "real position"
for pos,seq in m.search_instances(dnaSequence):
	#print (pos,seq.tostring())
	#print (pos,end=" ", sep="\t")
	print (pos+1,end=" ", sep="\t")

