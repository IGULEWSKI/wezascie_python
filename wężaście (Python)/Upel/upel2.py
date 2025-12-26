from math import log,sqrt
tab=[0]*10
def zad64(x,b)->str:
    tab=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    wyn=""
    while x!=0:
        wyn+=tab[x%b]
        x=x//b
    return wyn[::-1]
def zad65(a,b)->bool:
    def rozk(a)->list:
        w=int(log(a,10))+1
        tab=[0]*w
        i=0
        while a!=0:
            tab[i]=a%10
            a=a//10
            i+=1
        return tab[::-1]
    taba=rozk(a)
    tabb=rozk(b)
    if sorted(taba)==sorted(tabb):
        return True
    return False
def zad66(a):
    tab=[1]*(a+1)
    tab[0]=tab[1]=0
    for i in range(2,int(sqrt(a))+1):
        if tab[i]==1:
            for j in range(2*i,len(tab),i):
                tab[j]=0
    return tab[a]==1
def zad67()->int:
    b=input("wprowadz: ")
    tab=[]
    licz=0
    for i in range(len(b)):
        if b[i] == "0":
            tab.append(int(b[i-licz:i]))
            licz=0
        licz+=1
    return sorted(tab)[::-1][9]
wyn71=False
def zad71(tab,l=0)->bool:
    global wyn71
    if l==len(tab)-1:
        wyn71=True
    else:
        def czynniki(a)->set:
            i=2
            tab=[]
            while a>1:
                if a%i==0:
                    tab.append(i)
                    a=a//i
                else:
                    i+=1
            return set(tab)
        if l<len(tab):
            czyn=czynniki(tab[l])
            for el in czyn:
                zad71(tab,l+el)

def zad73(tab,N)->int:
    max=0
    for i in range(N):
        r=tab[i]-tab[i+1]
        l=0
        for j in range(i,N-1):
            if tab[j]-tab[j+1]==r:
                l+=1
            else:
                l=1
                r=tab[j]-tab[j+1]
            if l>max:
                max=l
        return max+1



    
print(zad73([3,6,9,12,15,11,2,4,6,8,13],5))




