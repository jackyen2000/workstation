#!/usr/bin/python
"""
Calculating Expected Offspring
Given: Six positive integers, each of which does not exceed 20,000. The integers
correspond to the number of couples in a population possessing each genotype pairing
for a given factor. In order, the six given integers represent the number of couples
having the following genotypes. 
Return: The expected number of offspring displaying the dominant phenotype in the next
generation, under the assumption that every couple has exactly two offspring.
"""
#data = [int(i) for i in open("rosalind_iev.txt").read().strip().split(" ")]
#weights = [1, 1, 1, 0.75, 0.5, 0]
#weights = [2*i for i in weights]
#print (sum([weights[i]*data[i] for i in range(len(data))]))


data = [int(i) for i in open("rosalind_iev").read().strip().split(" ")]
weights = [1, 1, 1, 0.75, 0.5, 0]
weights = [2*i for i in weights]
print (sum([weights[i]*data[i] for i in range(len(data))]))