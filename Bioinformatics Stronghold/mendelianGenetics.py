def MendelianGenetics(k,m,n):
    k = float(k)
    m = float(m)
    n = float(n)
    t = k + m + n
    AaAa = (m/t) * ((m-1)/(t-1))
    aaaa = (n/t) * ((n-1)/(t-1))
    Aaaa = ( ((m/t) *  (n/(t-1))) + ((n/t) *  (m/(t-1))) )
    return (1 - (AaAa*0.25 + aaaa + Aaaa*0.5))

print MendelianGenetics(18,17,15)
