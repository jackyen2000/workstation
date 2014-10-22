#from Bio import SeqIO
#from Bio.Alphabet import generic_dna

#for record in SeqIO.parse("dataset/rosalind_gc.fasta", "fasta", generic_dna):




	#print (record)

from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Alphabet import IUPAC, Gapped

alphabet = Gapped(IUPAC.ambiguous_dna)

alignment = AlignIO.read(open("dataset/test.fasta"), "fasta")
summary_align = AlignInfo.SummaryInfo(alignment)

summary_profile = AlignInfo.PSSM(alignment)
#consensus = summary_align.gap_consensus(threshold = 1.0, ambiguous = 'N', consensus_alpha= alphabet, require_multiple = 2)	

consensus = summary_align.dumb_consensus(threshold = 0, ambiguous = 'N', consensus_alpha = alphabet, require_multiple = 2)

#profile = AlignInfo.PSSM(alignment)

my_pssm = summary_align.pos_specific_score_matrix(consensus)


def profile(matrix):
    strings = matrix.split()

    default = [0] * len(strings[0])
    results = {
        'A': default[:],
        'C': default[:],
        'G': default[:],
        'T': default[:],
    }

    for s in strings:
        for i, c in enumerate(s):
            results[c][i] += 1

    return results


print (alignment)
#print (summary_align)
print (consensus)
#print (my_pssm)


