import re
import sys

def find_motif(motif, DNA):
    """Find the motif <motif> in the DNA string <DNA>
    """
    assert len(DNA) >= len(motif)
    #Search also for overlapping matches
    return [m.start() for m in re.finditer('(=?%s)' % motif, DNA)]



#f = open('rosalind_revc.txt', 'r')
#DNA = f.readline()
#f.close()




DNA = 'TTTGGGGTATTTGGGGTTTTGGGGCTCATTTGGGGCGTCATTTTGGGGTTTGGGGGTTTGGGGGGAGTTTGGGGTTTTTGGGGGATTTGGGGTTTGGGGGGCTCCCCTTTGGGGCTTTGGGGTTTGGGGATTTGGGGGTTCTTTGGGGAGCGTTTGGGGTTTGGGGCTTTGGGGTCTTTGGGGTTTGGGGTTTGGGGTCTGTTTGGGGTTTGGGGTTTTGGGGTTTGGGGTTTGGGGGCTTAGTTTGGGGTTTGGGGCGACTTTTTGGGGGTTTGGGGCTGGTTTGGGGTTTGGGGTTTTGGGGCCGGAAGTTTCTCACATACATTTGGGGTTTGGGGTTTGGGGCTTTGGGGTTTGGGGCAGTTTGGGGTTATTTTGGGGCTTCGTTTGGGGTTTGGGGTTTGGGGCTTTGGGGTTTGGGGTTTTTGGGGATACTGTTTGGGGTTTGGGGTTTGGGGTTTGGGGCAATTTGGGGCTTTGGGGTACGTTTGGGGGTTTGGGGTTTGGGGCTTTGGGGTTTTGGGGCTTTGGGGTTTGGGGATTTTGGGGCGTGACCAACGTTTGGGGACATTCGAATTTGGGGCATTTGGGGTTTGGGGTTTGGGGCTGTACCATTCTTAGTTTGGGGTTTGGGGCTTTGGGGTGGCTTTGGGGGTTTTGGGGCTTTGGGGGCTTTGGGGTTTGGGGCATTTGGGGGAATGAGGTTTGGGGTTTGGGGCGCTTTGGGGCCTTTTGGGGTTTGGGGTTTGGGGGTTTGGGGATCGTTCTTTGGGGGTTTGGGGGTCTTTGGGGACTTGTTTTGGGGGGCAGCTTTGGGGTTTGGGGGCCAGTTTGGGGTTTGGGGGAT'
motif = 'TTTGGGGTT'
print ("position of the motif: ", ' '.join(str(m+1) for m in find_motif(motif, DNA)))

print(' '.join(str(m+1) for m in find_motif(motif, DNA)))