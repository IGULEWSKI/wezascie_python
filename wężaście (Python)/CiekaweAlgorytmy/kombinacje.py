tabk1=[]

def Kombinacje(tab,tabf=[],i=0,tabk1=[]):
    if i==len(tab):
        tabk1.append(tabf)
    else:
        Kombinacje(tab,tabf[:],i+1)
        tabf.append(tab[i])
        Kombinacje(tab,tabf[:],i+1)
    return tabk1
def Kombinacjepowt(tab,k,tabf=[],i=0,m=0,tabk2=[]):
    if i==k:
        tabk2.append("".join(tabf))
    else:
        for j in range(m,len(tab)):
            tabf.append(tab[j])
            Kombinacjepowt(tab,k,tabf[:],i+1,m)
            tabf.remove(tab[j])
            m+=1
    return tabk2
def Permutacje(tab,l=0,tabk=[]):
    tabc=tab[:]
    if l==len(tab):
        tabk.append(tab)
    for i in range(l,len(tab)):
        tabc[l],tabc[i]=tabc[i],tabc[l]
        Permutacje(tabc,l+1)
    return tabk
            

tabk2=Kombinacjepowt(["1","2","3","4","5","6","7","8","9","0"],3)
print(tabk2,len(tabk2))
print(Kombinacje(['3','2','1']))