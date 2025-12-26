from math import sqrt
def Prime(a):
    if a<2:
        return 0
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return 0
    return 1
# n=10000000000
# tab=[1]*(n+1)
# tab[0]=0
# tab[1]=0
def Sito(tab):
    for i in range(2,int(sqrt(len(tab))+1)):
        if tab[i]==1:
            for j in range(2*i,len(tab),i):
                tab[j]=0
    return tab

for i in range(100000000000,10000000000,-1):
    a=str(i)
    if a[::-1]==a:
        if len(set(a))==6:
            if Prime(i)==1:
                print(i)
                break
