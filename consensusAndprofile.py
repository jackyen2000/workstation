#from Bio import SeqIO
#from Bio.Alphabet import generic_dna

#for record in SeqIO.parse("dataset/rosalind_gc.fasta", "fasta", generic_dna):




	#print (record)
from Bio import SeqIO
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Alphabet import IUPAC, Gapped
from Bio.SubsMat import FreqTable
from Bio import motifs

alphabet = Gapped(IUPAC.ambiguous_dna)


sequences = []
handle = open("dataset/test.fasta","rU")
#record_index = SeqIO.index("dataset/test.fasta", "fasta")
for record in SeqIO.parse(handle,"fasta"):
	#print (record.id)
	#print (record.seq)

	#instances = sequences.append(record.seq)
#m = motifs.create(record.seq)
	
	sequences = list(record.seq)
	m = motifs.create(sequences)
	#counts = m.counts

	print (sequences)
	print (m)
	#print (counts, end="")
#print (m.counts)

	#alignment = AlignIO.read(open("dataset/test.fasta"), "fasta")
#alignment = AlignIO.read(dna,"fasta")


#summary_align = AlignInfo.SummaryInfo(alignment)
#consensus = summary_align.dumb_consensus(threshold = 0, ambiguous = 'N', consensus_alpha = alphabet, require_multiple = 2)


#print (consensus)
#expect_freq = {
 #   'A' : .3,
 #   'G' : .2,
 #   'T' : .3,
 #   'C' : .2}

#e_freq_table = FreqTable.FreqTable(expect_freq, FreqTable.FREQ, IUPAC.unambiguous_dna)

#info_content = summary_align.information_content(0, 8, e_freq_table = e_freq_table, chars_to_ignore = ['N'])




#m = motifs.create(alignment)





#my_pssm = summary_align.pos_specific_score_matrix(consensus, chars_to_ignore = ['N'])

#profile = summary_align._get_letter_freqs(consensus, residue_num = 4, all_records = consensus, letters = 'T')

#print (alignment)
#print (consensus)

#print (e_freq_table)


#print (info_content)


#print (my_pssm)
#print (profile)


