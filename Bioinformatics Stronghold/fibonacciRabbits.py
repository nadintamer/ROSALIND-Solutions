def rabbits(n,k):
    total, rabbits = 1,1
    for i in range(n-1):
        total,rabbits = rabbits,k*total+rabbits
    return total
    

print rabbits(6,2)
