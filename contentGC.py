
##use biopython
from Bio import SeqIO
from Bio.SeqUtils import GC


def parse_fasta(s):
	results = {}
	strings = s.strip().split('>')

	for s in strings:
		if len(s) == 0:
			continue

		parts = s.split()
		label = parts[0]
		bases = ''.join(parts[1:])

		results[label] = bases
		
	return results


def gc_content(s):
	n = len(s)
	m = 0

	for c in s:
		if c == 'G' or c == 'C':
			m += 1

	return 100 * (float(m) / n)



if __name__ == "__main__":



	
#with open(output_file) as out_file:
#    for fasta in fasta_sequences:
#        name, sequence = fasta.id, fasta.seq.tostring()
#        new_sequence = some_function(sequence)
#        write_fasta(out_file)



	small_dataset = """
	>Rosalind_6404
	CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
	TCCCACTAATAATTCTGAGG
	>Rosalind_5959
	CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
	ATATCCATTTGTCAGCAGACACGC
	>Rosalind_0808
	CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
	TGGGAACCTGCGGGCAGTAGGTGGAAT
	"""

	#generate object contains sequence ID and sequence
	#fasta_sequences = SeqIO.parse(open('dataset/rosalind_gc.fasta'),'fasta')


	#dna_Sequence = {}
	#for seq_record in SeqIO.parse("dataset/rosalind_gc.fasta", "fasta"):


		#dna_Sequence[seq_record.id] = seq_record.seq

		#rec = len(seq_record)
		gc_values = sorted(GC(seq_record.seq) for seq_record in SeqIO.parse("dataset/rosalind_gc.fasta", "fasta"))
		#seq_id = seq_record.id
		#print (seq_id)
		#gc_values = GC(seq_record.seq) 
		print (gc_values)



		#for a_key, a_value in dna_Sequence.iteritems():
		#	print (a_key, a_value)
		#print(dna_Sequence)
		#print(repr(seq_record.seq))
		#print(len(seq_record))
		#print (seq_record.seq)
	#large_dataset = open('dataset/rosalind_gc.fasta').read()
		#k = for seq_record.id
		#print (k)

	#results = parse_fasta(large_dataset)
	#results = dict([(k, gc_content(v)) for k, v in results.iteritems()])

	#results = dict([(k, gc_content(v)) for k, v in results.iteritems()])

	#gcresults = gc_content(repr(seq_record.seq))

    #from Bio.SeqRecord import SeqRecord

	#def make_rc_record(record):
    #"""Returns a new SeqRecord with the reverse complement sequence."""
    #return SeqRecord(seq = record.seq.reverse_complement(), \
    # id = "rc_" + record.id, \
    #             description = "reverse complement")

	#from Bio import SeqIO
	#records = map(make_rc_record, SeqIO.parse("ls_orchid.fasta", "fasta"))
	#SeqIO.write(records, "rev_comp.fasta", "fasta")


	


	
	#gcresults = map(GC, seq_record.seq)
	#for key, value in gcresults.iteritems() :
 	#	print (key, value)
	#print (SeqIO.str(gcresults))


	highest_k = None
	highest_v = 0

	#for k, v in results.iteritems():
	#    if v > highest_v:
	#        highest_k = k
	#        highest_v = v

	#print (fasta_sequences)
	#print (results)        
	#print (highest_k)
	#print ('%f%%' % highest_v)
