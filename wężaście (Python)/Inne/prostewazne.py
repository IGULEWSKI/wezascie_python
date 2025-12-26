import math
tab=[11,2,3,45,2,18]
tab2=tab[:]
def bubblesort(tab)->list:
    for i in range(len(tab)):
        for j in range(len(tab)-1-i):
            if tab[j]<=tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab
def nwd(a,b)->int:
    while b>0:
        a,b=b,a%b
    return a
def nww(a,b)->int:
    return a*b//nwd(a,b)
def prime(a)->bool:
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True