def Primes():
    p=2
    tab=[2]
    yield p
    while True:
        p+=1
        for el in tab:
            if p%el==0:
                break
        else:
            yield p
            tab.append(p)

prim=Primes()
def twins():
    g=Primes()
    w1=next(g)
    while True:
        w2=next(g)
        if w2-w1==2:
            yield w1,w2
        w1=w2
l=0
for a,b in twins():
    print(a,b)
    l+=1
    if l==20:
        break