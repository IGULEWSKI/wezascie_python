N=int(input())
tab=[]
for _ in range(N):
    nap1=str(input())
    a,bc=nap1.split('+')
    b,c=bc.split('=')
    tab.append((a,b,c))

tabcyf=["1","2","3","4","5","6","7","8","9"]
def Permutacje(tab,l=0,tabk=[]):
    tabc=tab[:]
    if l==len(tab):
        tabk.append(tab)
    for i in range(l,len(tab)):
        tabc[l],tabc[i]=tabc[i],tabc[l]
        Permutacje(tabc,l+1)
    return tabk
def sklejacz(a,tab):
    nap=''
    dictlit={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8}
    for el in a:
        nap+=tab[dictlit[el]]
    return int(nap)
perm=Permutacje(tabcyf)
guard2=False
for cyferki in perm:
    guard=True
    for row in tab:
        w1,w2,w3=row
        a=sklejacz(w1,cyferki)
        b=sklejacz(w2,cyferki)
        c=sklejacz(w3,cyferki)
        if a+b!=c:
            guard=False
            break
    if guard==True:
        print("".join(cyferki))
        guard2=True
        break
if guard2==False:
    print("BRAK")


    
    