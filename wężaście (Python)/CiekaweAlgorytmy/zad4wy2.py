from math import gcd
from random import randint
# pow(a,b,c)= a**b mod c


def FermatProb(p,n) -> bool:# n liczba prób
    if p<2: 
        return False
    if p==2 or p==3:
        return True
    if p%2==0:
        return False
    for _ in range(n):
        a=randint(2,p-1)
        if gcd(p,a)!=1:
            return False
        if pow(a,p-1,p)!=1:
            return False
    return True

def Zadanko(a) -> int:
    a=str(a)
    suma=0
    for el in a:
        el=int(el)
        suma+=el**len(a)
    return suma
tabk2=[]

def KombinacjePowt(tab,k,tabf=[],i=0,m=0) -> None:
    if i==k:
        tabk2.append("".join(tabf))
    else:
        for j in range(m,len(tab)):
            tabf.append(tab[j])
            KombinacjePowt(tab,k,tabf[:],i+1,m)
            tabf.remove(tab[j])
            m+=1
def Licz(a) -> list:
    a=str(a)
    counter=[0,0,0,0,0,0,0,0,0,0]
    for el in a:
        counter[int(el)]+=1
    return counter

print(Zadanko("35452590104031691935943")==35452590104031691935943,FermatProb(35452590104031691935943,1000))
print(Zadanko("449177399146038697307")==449177399146038697307,FermatProb(449177399146038697307,1000))
print(Zadanko("28116440335967")==28116440335967,FermatProb(28116440335967,1000))
for i in range(17,30):
    print(i,"-------------------")          
    KombinacjePowt(["1","2","3","4","5","6","7","8","9","0"],i)
    for el in tabk2:
        ab=Zadanko(el)
        if len(str(ab))==len(el):
            if FermatProb(ab,10):
                if Licz(el)==Licz(ab):
                    print(el,ab)
    tabk2=[]
#2
#3
#5
#7
#28116440335967
#449177399146038697307
#35452590104031691935943



#małe twierdzenie fermata liczby pierwsze algorytm probalistyczny