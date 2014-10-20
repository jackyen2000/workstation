#import the IUPAC alphbet definitions
from Bio.Alphabet import IUPAC

#import the Sequence class definition (note: the name of the class is "Seq")
from Bio.Seq import Seq
from Bio import SeqIO


import argparse
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

#Create a messenger RNA Sequence
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)

f = open('dataset/test.fasta', 'r')
rnaSequence = f.readlines()
f.close()


rnaSequence_record = " "
for record in SeqIO.parse("dataset/test.fasta","fasta",IUPAC.ambiguous_rna):




    s = Seq(args.dataset.read().rstrip(), generic_rna)
    print(s.translate(stop_symbol=''))

#Now for the new part

#Translate with the standard translation table
#my_protein_1 = messenger_rna.translate()

	protein_translate = rnaSequence_record.translate()


#display the results
#print ("my mRNA sequence is ",messenger_rna)
#print ("my_protein_1 is ",my_protein_1)
#print ("My_protein's alphabet is ",my_protein_1.alphabet)


print (rnaSequence_record.seq)

# You can also translate directly from a coding DNA
# Creat a DNA sequence
#coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)

#my_protein_2 = coding_dna.translate()
#print "my_proteen_2, translated from DNA, is "
#print my_protein_2

# If you start with mitochonbdrial DNA, you can us a different translation table
#my_protein_3 = coding_dna.translate(table="Vertebrate Mitochondrial")

#print "my_protein_3, tranlated from Mitochondrial DNA, is "
#print my_protein_3

# Notice that the default translation will just go ahead and proceed blindly through
# a stop codon (GAA). 
# If you are aware that you are translating some kind of open reading frame 
# and want to just see everything up until the stop codon, 
# this can be easily done by setting to_stop=True

#my_protein_4 = coding_dne.translate(to_stop=True)

#print "my_protein_4, tranlated from DNA, stopping at the ifrst stop codon, is "
#print my_protein_4
