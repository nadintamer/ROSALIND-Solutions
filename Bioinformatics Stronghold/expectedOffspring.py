def expectedOffspring(a,b,c,d,e,f):
    total = 0
    #a
    total += 2*a
    #b
    total += 2*b
    #c
    total += 2*c
    #d
    total += 1.5*d
    #e
    total += 1*e
    #f
    total += 0*f
    return total

print expectedOffspring(16099,19472,17438,18949,17143,19911)
    
