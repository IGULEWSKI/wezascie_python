tabk1=[]

def PodZbiory(tab,tabf=[],i=0,tabk1=[]):
    if i==len(tab):
        tabk1.append(tabf)
    else:
        PodZbiory(tab,tabf[:],i+1)
        tabf.append(tab[i])
        PodZbiory(tab,tabf[:],i+1)
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
def Wariacje(tab:[list])->[list]:
    pom=[[]]
    for el in tab:
        pom= [x+[y] for x in pom for y in el] #najpierw tworzy tablice z samymi elementami z pierwszej następnie towrzy dla wszystkich z elementami z pierwszej tworzy wszystkie z drugiej itd. okazuje się że ma to ogromną złożoność
    return pom
            

tabk2=Kombinacjepowt(["1","2","3","4","5","6","7","8","9","0"],3)
print(tabk2,len(tabk2))
print(PodZbiory(['3','2','1',"4"]))