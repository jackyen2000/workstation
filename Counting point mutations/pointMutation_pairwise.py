from Bio import pairwise2
from Bio import SeqIO



		#t = 0

		#q = 0
#for seq_record in SeqIO.parse("dataset/test.fasta", "fasta"):
	#for q in SeqIO.parse("dataset/rosalind_subs.txt", "fasta"):


f = open('dataset/rosalind_hamm.txt', 'r')
dnaSequence = f.readlines()
f.close()

#print (dnaSequence)
#print (dnaSequence[0])
#print (dnaSequence[1])


seq1 = dnaSequence[0]
seq2 = dnaSequence[1]
	#t = seq_record[0]
	#a = seq_record[1]
#compare = pairwise2._align(seq1,seq2)

count = 0
mismatches = 0 
#def sequence_compare(seq1, seq2):
len1= len(seq1)
len2= len(seq1)
#        mismatches = []
#        for pos in range (0,min(len1,len2)) :
#              if seq1[pos] != seq2[pos]:
#                  count = count+1

for c in range (0, min(len1, len2)):
    if seq1[c] == seq2[c]:
        count = count + 1
    else:
        mismatches = mismatches + 1
  #      print (seq1)
        #print (mismatches,sep=" ")
 #       print (seq2)
#print (count)
#sequence_compare(seq1,seq2)
print ("this is the number of matches: ",count)
print ("this is the number of mismatches: ",mismatches)
print (mismatches)

#print (seq1+seq2,end="\n")

#print (compare)

	#print (seq_record)
	#print (a)
	#a = pairwise2.align(t.seq, q.seq, one_alignment_only=1, score_only=1)
	#print (t.id, "\t", q.id, "\t", a)
	#print (a)




