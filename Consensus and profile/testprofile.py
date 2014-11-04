from Bio import SeqIO
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Alphabet import IUPAC, Gapped
from Bio.SubsMat import FreqTable
from Bio import motifs

#import numpy as np





## Dados de exemplo
s = """
ATCCAGCT
GGGCAACT
ATGGATCT
AAGCAACC
TTGGAACT
ATGCCATT
ATGGCACT
""".split()
#############################################################

def consensus(strings):
	profile = {'A': [], 'C': [], 'G': [], 'T': []}
n = len(strings)
m = len(strings[0])

# Matriz de profile
scolumns = [[[list(string) for string in strings][i][j] for i in range(n)] for j in range(m)]
for column in scolumns:
	for nucleus in profile.keys():
		profile[nucleus].append(column.count(nucleus))

# Consensus retornando somente o primeiro resultado
result = ""
nuclei = profile.keys()
pcolumns = [[(nucleus, profile[nucleus][i]) for nucleus in nuclei] for i in range(len(profile[nuclei[0]]))]
for column in pcolumns:
	record = column[0]

for nucleus, freq in column[1:]:
	if freq > record[1]: record = (nucleus, freq)
	result += record[0]

return result, profile

print (consensus(s)[0])
print ("A:",consensus(s)[1]['A'])
print ("C:",consensus(s)[1]['C'])
print ("T:",consensus(s)[1]['T'])
print ("G:",consensus(s)[1]['G'])