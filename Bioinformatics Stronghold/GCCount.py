from Bio import SeqIO
DNAfile = SeqIO.parse("GCCount.fasta","fasta")
percents = []
def GCCounter(dna):
    count = 0.0
    gc = 0.0
    for x in dna:
        count += 1
        if x == "C" or x == "G":
            gc += 1
    percent = (gc/count)*100
    return percent

for fasta in DNAfile:
    name, sequence = fasta.id, fasta.seq.tostring()
    percents.append([name, GCCounter(sequence)])

maxi = 0
index = 0
for x in percents:
    if x[1] > maxi:
        maxi = x[1]
        index = percents.index(x)

print percents[index][0]
print percents[index][1]

        
    



