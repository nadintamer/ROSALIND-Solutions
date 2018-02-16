def motifDNA(dna, motif):
    a = len(motif)
    places = []
    for x in range(len(dna)-a+1):
        if dna[x:x+a] == motif:
            places.append(x+1)
    for y in places:
        print y,
            
        
