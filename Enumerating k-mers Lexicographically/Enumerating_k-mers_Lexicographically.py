import itertools


string = open("D:/python/dataset/rosalind_lexf.txt").read().strip()

#print (string)
#print ("first line is:")
#print (string.splitlines()[0])
#print ("second line is:")
#print (string.splitlines()[1])
#print (string[1])

#ss = "S G A Y W T N P M"
ss = string.splitlines()[0]
ss = "".join(ss.split())
n = int(string.splitlines()[1])
#n = 3

rs = [ "".join(r) for r in itertools.product(ss, repeat=n)] 
print ("\n".join(rs))