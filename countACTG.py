# Lab 2, Program 3
#
# Given a DNA sequence, count and report the number of A's, C's, T's,
# and G's in the sequence.
#
# This program is much like the program we wrote in class to
# count the number of A's in a DNA sequence.  The main difference
# is that it counts all four kinds of nucleotides, instead of just
# one.
#
# Consider how you might solve this problem on paper.  If you're like
# me and you have trouble keeping track of four numbers in your head
# at once, you might do what I would do: count the nucleotides separately.
# First, go through the sequence, count the A's, and write the answer
# down.  Then, go through the sequence, count the C's, and write that
# answer down.  And so on.
#
# Now, Python doesn't have the problem that I have: it can definitely
# keep track of four numbers at a time.  So, we'll have it count all
# four kinds of nucleotides simultaneously.

#if __name__ == "__main__":

#!/usr/bin/env python

dnaSequence = ("atcgatgagagctagcgata")

aCount = 0
cCount = 0
tCount = 0
gCount = 0

for c in dnaSequence:
    if c == 'a':
        aCount = aCount + 1
    elif c == 'c':
        cCount = cCount + 1
    elif c == 't':
        tCount = tCount + 1
    elif c == 'g':
        gCount = gCount + 1

print (("Number of A's in sequence:"),  aCount)
print (("Number of C's in sequence:"),  cCount)
print (("Number of T's in sequence:"),  tCount)
print (("Number of G's in sequence:"),  gCount)
