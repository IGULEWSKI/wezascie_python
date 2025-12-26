from math import sqrt
from copy import deepcopy
#N=list(input().strip())
N=list("13171923293137414347")
def sumtab(tab):
    kon=[]
    for el in tab:
        kon+=el
    return kon
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
def PodPier(ciag) -> list:
    tab=[]
    for wiel in range(len(ciag)-1,-1,-1):
        for i in range(len(ciag)-wiel):
            subc=ciag[i:i+wiel+1]
            if None not in subc and len(subc)==len(set(subc)):
                if Prime(int("".join(subc))):
                    tab.append((subc,i,i+wiel))
    return tab

def sklejacz(sklej,tab,N,k=-1,tabf=[]):
    sklej=deepcopy(sklej)
    guardbreak=False
    l=0
    licz=tabp.count(k+1)
    if k+1 not in tabp:
        guardbreak=True
    if k==-1:
        k=len(sklej[0])-1
    if k==len(N)-1:
        tabf.append(len(sklej))
    for el in tab:
        if guardbreak==True:
            break
        ele=el[0]
        pocz=el[1]
        kon=el[2]
        if pocz==k+1:
            l+=1
            sklej.append(ele)
            sklejacz(sklej,tab,N,kon,tabf)
            sklej.pop()
            if licz==l:
                guardbreak=True

    return tabf


        

tab=PodPier(N)
start=[el[0] for el in tab if el[1]==0]
for el in tab:
    print(el)
print(start)
tabf2=[]
tabp=[el[1] for el in tab]
for sklej in start:
    tabf2+=sklejacz([sklej],tab,N)
if len(tabf2)==0:
    print("BRAK")
else:
    print(min(tabf2))