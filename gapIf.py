# Lab 2, Program 1
#
# Given a DNA sequence, find out whether there is a gap.
#
# This is one solution to the problem, which involves first counting
# the number of gaps, then deciding whether there were any gaps by
# seeing if the count is more than zero.

dnaSequence = "atcgatgagagctagcgata"

gapCount = 0

for c in dnaSequence:
    if c == '-':
        gapCount = gapCount + 1

if gapCount > 0:
    print "There is a gap in the sequence."
else:
    print "There is no gap in the sequence."

    
    