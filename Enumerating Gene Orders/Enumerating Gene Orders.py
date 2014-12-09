import itertools

how_many = open("D:/python/dataset/rosalind_perm.txt").read().strip()

#print (how_many)
#print (type(how_many))
#how_many = 3
perms = itertools.permutations(range(1, int(how_many) + 1))


#perms = itertools.permutations(range(1, 7 + 1))

#print (len(perms))

#print (len(perms))

list_perms = list(perms)
print (len(list_perms))

for perm in list_perms:
    strings = [str(value) for value in perm]
    print (' '.join(strings))