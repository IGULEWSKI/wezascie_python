N=int(input("wielkość macierza"))
cyferki=[i for i in range(0,N)]
tabf=[]
for _ in range(N):
    tab1=input("Podaj wiersz macierza:").split(',')
    tab1=list(map(int,tab1))
    tabf.append(tab1)
print(tabf)
def permutacje(tab,l=0,tabk=[]):
    tabc=tab[::]
    if l==len(tab):
        tabk.append(tab)
    for i in range(l,len(tab)):
        tabc[l],tabc[i]=tabc[i],tabc[l]
        permutacje(tabc,l+1)
    return tabk
Sn=permutacje(cyferki)
def sprparzy(tab):
    inw=0
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            if tab[i]>tab[j]:
                inw+=1
    return (-1)**inw
suma=0
for el in Sn:
    ilo=1
    for i in range(N):
        ilo*=tabf[i][el[i]]
    suma+=sprparzy(el)*ilo
print(suma)

