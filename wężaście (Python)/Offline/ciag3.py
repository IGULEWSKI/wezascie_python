from math import gcd
tab=[]
miano=[]
N=int(input())
for _ in range(N):
    a,b=input().strip().split()
    tab.append((int(a),int(b)))
    miano.append(int(b))
def nww(tab,p=0):
    if p==len(tab)-2:
        return tab[p]*tab[p+1]//gcd(tab[p+1],tab[p])
    a=nww(tab,p+1)
    b=tab[p]
    return b*a//gcd(a,b)
def ułamekroznica(ul1,ul2)->tuple:
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    fmian=mian1*mian2
    flicz=flicz1-flicz2
    dziel=gcd(flicz,fmian)
    return (flicz//dziel,fmian//dziel)
def ułameksuma(ul1,ul2)->tuple:
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    fmian=mian1*mian2
    flicz=flicz1+flicz2
    dziel=gcd(flicz,fmian)
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
    return flicz1<flicz2
def ułamektocos(ul1,ul2):#ul1<ul2
    licz1,mian1=ul1
    licz2,mian2=ul2
    flicz1=licz1*mian2
    flicz2=licz2*mian1
    return flicz1%flicz2
rozz=[]
mini=ułamekroznica(tab[1],tab[0])
for i in range(len(tab)-1):
    ul1=tab[i]
    ul2=tab[i+1]
    r=ułamekroznica(ul2,ul1)
    rozz.append(r[0])
    if ułamekmniejszy(r,mini):
        mini=r

n=2
mini=(gcd(*rozz),nww(miano))
    

#ciag=[]
for i in range(len(tab)-1):
    ul1=tab[i]
    ul2=tab[i+1]
    #ciag.append(tab[i])
    r=ułamekroznica(ul2,ul1)
    m=ułamekwielo(r,mini)
    for _ in range(1,m):
        ula=ułameksuma(ul1,mini)
        print(*ula)
        #ciag.append(ula)
        ul1=ula
#ciag.append(tab[-1])
#print(ciag)
