

from Bio.Seq import Seq

dna = ("GATGGAACTTGACTACGTAAATT")


#f = open('rosalind_dna.txt', 'r')
#dna = f.readline()
#f.close()

#print (dnaSequence)


trans = {           \
        'A':'A',  \
        'T':'U',  \
        'C':'C',  \
        'G':'G',  \
}

#for base in dna[::-1]:
#    try:
#        base = sub[base]
#    except KeyError:
#        pass
#    r_dna += base

#print ("This is the original DNA strand: ", dna)
#print ("This is the reversed DNA strand: ", r_dna)