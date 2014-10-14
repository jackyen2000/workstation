

#from Bio.Seq import Seq

#dnaSequence = ("GATGGAACTTGACTACGTAAATT")


f = open('rosalind_rna.txt', 'r')
dnaSequence = f.readline()
f.close()

#print (dnaSequence)


def transcribe(dna): 
     """Return dna string as rna string.""" 
     return dna.replace('T', 'U')       


#print("This is the transcribed RNA sequence from DNA input: ",transcribe(dnaSequence))

print(transcribe(dnaSequence))


#my_dna
#Seq('AGTACACTGGT', DNAAlphabet())
#my_dna.transcribe()
#Seq('AGUACACUGGU', RNAAlphabet())


#for base in dna[::-1]:
#    try:
#        base = sub[base]
#    except KeyError:
#        pass
#    r_dna += base

#print ("This is the original DNA strand: ", dna)
#print ("This is the reversed DNA strand: ", r_dna)