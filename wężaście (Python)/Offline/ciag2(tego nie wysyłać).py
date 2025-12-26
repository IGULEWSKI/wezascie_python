from math import inf
tab=[]
N=int(input())
for _ in range(N):
    a,b=input().strip().split()
    tab.append((int(a),int(b)))

def nwd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def ułamekroznica(ul1,ul2)->tuple:
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    fmian=mian1*mian2
    flicz=flicz1-flicz2
    dziel=nwd(flicz,fmian)
    return (flicz//dziel,fmian//dziel)
def ułameksuma(ul1,ul2)->tuple:
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    fmian=mian1*mian2
    flicz=flicz1+flicz2
    dziel=nwd(flicz,fmian)
    return (flicz//dziel,fmian//dziel)
def ułamekwielo(ul1,ul2):
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    if flicz2==0:
        return 0
    return abs(flicz1//flicz2)
def ułamekmniejszy(ul1,ul2):#ul1<ul2
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    return abs(flicz1)<abs(flicz2)
mini=ułamekroznica(tab[1],tab[0])
for i in range(len(tab)-1):
    ul1=tab[i]
    ul2=tab[i+1]
    r=ułamekroznica(ul2,ul1)
    if ułamekmniejszy(r,mini):
        mini=r
for i in range(len(tab)-1):
    ul1=tab[i]
    ul2=tab[i+1]
    r=ułamekroznica(ul2,ul1)
    m=ułamekwielo(r,mini)
    for _ in range(1,m):
        ula=ułameksuma(ul1,mini)
        print(*ula)
        ul1=ula



