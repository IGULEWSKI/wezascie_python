N=int(input())
tab=[]
for _ in range(N):
    kast=list(input())
    tab.append(kast)
def ukrp(tab)->list:
    maxx=0
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            pot=tab[i:j+1]
            if pot[::-1]==pot and len(pot)>=5:
                lpot=len(pot)
                if lpot>maxx:
                    maxx=lpot
                    maxa=pot
    if maxx>0:
        return tuple(maxa)
    return False

def skaner(tab:list[list],n):
    final=set()
    for i in range(n):
        wiersz = tab[i]
        kolumna=[]
        skos1=[tab[i][0]]
        skos2=[tab[i][n-1]]
        skos3=[tab[n-i-1][n-1]]
        skos4=[tab[n-i-1][0]]
        l=i
        for j in range(n):
            kolumna.append(tab[j][i])
        for k in range(1,n):
            if i-k>=0:
                skos1.append(tab[i-k][k])
                skos2.append(tab[i-k][n-1-k])
            if (n-i-1)+k<n:
                skos3.append(tab[(n-i-1)+k][n-1-k])
                skos4.append(tab[(n-i-1)+k][k])
        pwiersz=ukrp(wiersz)
        pkolumna=ukrp(kolumna)
        pskos1=ukrp(skos1)
        pskos2=ukrp(skos2)
        pskos3=ukrp(skos3)
        pskos4=ukrp(skos4)
        if i==n-1:
            pskos1=False
            pskos2=False
        if pwiersz!=False:
            if pwiersz in final:
                print(''.join(pwiersz))
            final.add(pwiersz)
        if pkolumna!=False:
            if pkolumna in final:
                print(''.join(pkolumna))
            final.add(pkolumna)
        if pskos1!=False:
            if pskos1 in final:
                print(''.join(pskos1))
            final.add(pskos1)
        if pskos2!=False:
            if pskos2 in final:
                print(''.join(pskos2))
            final.add(pskos2)
        if pskos3!=False:
            if pskos3 in final:
                print(''.join(pskos3))
            final.add(pskos3)
        if pskos4!=False:
            if pskos4 in final:
                print(''.join(pskos4))
            final.add(pskos4)
        
skaner(tab,N)


