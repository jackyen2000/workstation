# Lab 2, Program 2
#
# Given a DNA sequence, count the number of gaps in the sequence.
#
# This program is very much like the program we wrote in class to
# count the number of A's in a DNA sequence.  The only difference
# is that we're counting '-' characters instead of 'a' characters.



dnaSequence = ("atcga-tgag-agctagcg-ata")

gapCount = 0

for c in dnaSequence:
    if c == '-':
        gapCount = gapCount + 1

#print (gapCount)
print (("Number of gaps in sequence:"), gapCount)