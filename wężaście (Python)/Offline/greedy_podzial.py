from math import sqrt
N=list("373737373737373737373737373737373737373737373737373737373737373737373737373737373737373737373737373")
def Prime(a)->bool:
    if a<2:
        return False
    if a==2:
        return True
    if a%2==0:
        return False
    for i in range(3,int(sqrt(a))+1,2):
        if a%i==0:
            return False
    return True

def fin(bciag)->list:
    fintab=[]
    guard=True
    def MaxPPC(ciag1) -> list:
        nonlocal fintab
        nonlocal guard
        nonlocal s
        for wiel in range(len(ciag)-1-s,-1,-1):
            for i in range(len(ciag)-wiel):
                subc=ciag[i:i+wiel+1]
                if None not in subc and len(subc)==len(set(subc)):
                    if Prime(int("".join(subc))):
                        fintab.append(subc)
                        for i in range(i,i+wiel+1):
                            ciag[i]=None
                        return None
        guard=False
    s=0
    while s<len(bciag):
        ciag=bciag[:]
        while guard==True:
            MaxPPC(ciag)
        s+=1
        licz=ciag.count(None)
        if licz==len(ciag):
            print(len(fintab))
            return None
    print("BRAK")
fin(N)