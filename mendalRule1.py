# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="chiyuyen"
__date__ ="$Sep 23, 2014 1:40:59 PM$"


#Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
#k t are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#Return the probability that two randomly selected mating organisms 
#will produce an individual possessing a dominant allele

f = open('rosalind_mendel.txt', 'r')
sets = f.readlines()
f.close()


for population in sets:
    k, m, n = map(float, population.split())
    t = k+m+n
    pk = k/t
    pm = m/t
    pn = n/t

    #Total probability
    prob = 1
    #Minus the probability of both parents being homozygous recessive
    prob -= pn*((n-1)/(t-1))
    #Minus twice the probability of one being homozygous recessive and the other
    #one heterozygous with the recessive allele (this is the 0.5)
    prob -= 2*pn*(m/(t-1))*0.5
    #Minus the probability of both being heterozygous with the recessive allele (this is the 0.25)
    prob -= pm*((m-1)/(t-1))*0.25
    print prob