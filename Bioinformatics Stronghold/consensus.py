# -*- coding: utf-8 -*-
from Bio import SeqIO
DNAfile = SeqIO.parse("consensus.fasta","fasta")
records = list(SeqIO.parse("consensus.fasta","fasta"))

Acount = []
Ccount = []
Gcount = []
Tcount = []

first_record = records[0]

for x in range(len(first_record.seq)):
    Acount.append(0)
    Ccount.append(0)
    Gcount.append(0)
    Tcount.append(0)

for fasta in DNAfile:
    name, sequence = fasta.id, str(fasta.seq)
    for x in range(len(sequence)):
        if sequence[x] == "A":
            Acount[x] += 1
        elif sequence[x] == "C":
            Ccount[x] += 1
        elif sequence[x] == "G":
            Gcount[x] += 1
        elif sequence[x] == "T":
            Tcount[x] += 1

def consensus(A, C, G, T):
    new = ""
    for x in range(len(A)):
        if A[x] == max(A[x], C[x], G[x], T[x]):
            new += "A"
        elif C[x] == max(A[x], C[x], G[x], T[x]):
            new += "C"
        elif G[x] == max(A[x], C[x], G[x], T[x]):
            new += "G"
        elif T[x] == max(A[x], C[x], G[x], T[x]):
            new += "T"
    return new
         
print consensus(Acount, Ccount, Gcount, Tcount)
print "A:",
for x in Acount:
    print x,
print
print "C:",
for x in Ccount:
    print x,
print
print "G:",
for x in Gcount:
    print x,
print
print "T:",
for x in Tcount:
    print x,



