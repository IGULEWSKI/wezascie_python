def nsuma(tab,S,N=3,start=0):
    if N==0:
        return S==0
    for i in range(start,len(tab)):
        if nsuma(tab,S-tab[i],N-1,i+1)==True:
            return True
    return False
def nsuma2(tab,S,N=3,start=0):
    if N==0:
        return S==0
    wyn=False
    for i in range(start,len(tab)):
        wyn=wyn or nsuma2(tab,S-tab[i],N-1,i+1)
    return wyn
print(nsuma2([5,6,4,2,1,2],115))

    