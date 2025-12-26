tab=[[1,2,3],[4,5,6],[7,8,9]]
tab1=[2,5,3,2,3]
for i in range(len(tab)*len(tab[0])):
    k=i%len(tab[0])
    w=i//len(tab[0])
    print(tab[w][k])
licz=0
def nkiilo(tab,d,n,p=0):
    if n==1:
        global licz
        for i in range(p,len(tab)):
            if tab[i]==d:
                licz+=1
    else:
        for i in range(p,len(tab)):
            if d%tab[i]==0:
                nkiilo(tab,d//tab[i],n-1,i+1)
nkiilo(tab1,30,3)
print(licz)
        
    