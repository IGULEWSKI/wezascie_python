from math import sqrt
#N=list(input())
N=list("13171923293137414347")
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
    htab=[[] for i in range(len(N))]
    def MaxPPC() -> list:
        nonlocal htab
        fintab=[]
        ciag=bciag[:]
        guard=True
        id=0
        pom={}
        for wiel in range(len(ciag)-1,-1,-1):
            for i in range(len(ciag)-wiel):
                subc=ciag[i:i+wiel+1]
                if len(subc)==len(set(subc)) and subc[0]!="0" and Prime(int("".join(subc)))==True:
                    pom[id]=len(subc)
                    fintab.append(subc)
                    for j in range(i,i+wiel+1):
                        htab[j].append(id)
                    id+=1
        def Wariacje(tab:[list])->[list]:
            pom=[[]]
            for el in tab:
                pom= [x+[y] for x in pom for y in el] #najpierw tworzy tablice z samymi elementami z pierwszej następnie towrzy dla wszystkich z elementami z pierwszej tworzy wszystkie z drugiej itd. okazuje się że ma to ogromną złożoność
            return pom
        def Filtr(war,dic)->list:
            for pot in war:
                guard=True
                curid=pot[0]
                l=0
                for i in range(len(pot)):
                    if curid==pot[i]:
                        l+=1
                    else:
                        if l!=dic[curid]:
                            guard=False
                            break
                        l=1
                    curid=pot[i]
                if guard==True:
                    yield pot
        war=Wariacje(htab)
        print(len(war))
        fin=list(Filtr(war,pom))
        if len(fin)==0:
            print("BRAK")
        else:
            print(min([len(set(el)) for el in fin]))
        
    MaxPPC()
fin(N)

