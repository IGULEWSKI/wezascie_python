from math import sqrt
#N=list(input())
N=list(str(13171923293137414347))
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
def sklejacz(tab,N):
    tabf=[]
    for el in tab:
        sklej=[el[0]]
        p=el[1]
        k=el[2]
        guard2=False
        print('zmiana')
        while  True:
            print(sklej)
            guard2=False
            for el2 in tab:
                print(sklej,p,k,'ok')
                if el2[2]==p-1:
                    p=el2[1]
                    sklej.append(el2[0])
                    guard2=True
                elif el2[1]==k+1:
                    k=el2[2]
                    sklej.append(el2[0])
                    guard2=True
                if p==0 and k==len(N)-1:
                    break
            if guard2==False:
                break
        if p==0 and k==len(N)-1:
            tabf.append(sklej)
    if len(tabf)==0:
        print("BRAK")
    else:
        print([len(el) for el in tabf])

            
                



        

print(N)
tab=PodPier(N)
for el in tab:
    print(el)
sklejacz(tab,N)