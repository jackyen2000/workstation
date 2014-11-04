#!/usr/bin/python
"""
Mortal Fibonacci Rabbits
Given: Positive integers n <= 100 and m <= 20.
Return: The total number of paris of rabbits that will remain after the n-th month if all rabbits live for 
m months. 
"""
N, M = open("rosalind_fibd.txt").read().strip().split(" ")
N = int(N)
M = int(M)

def fib(n,m):
  rabbits = dict([(i,0) for i in range(m)])
  rabbits[m-1] = 1
  a = 1
  b = 1
  while n > 0:
    n -= 1
    t = b
    b = a+b
    a = t
    for i in range(m-1): rabbits[i] = rabbits[i+1]
    new_rabbits = b-a
    rabbits[m-1] = new_rabbits
    b = sum([rabbits[i] for i in range(1,m)])
  return sorted(rabbits.items())[-1][1]

print (fib(N,M))