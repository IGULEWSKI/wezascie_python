import time
start=time.time()
N=int(input())
inputt=[]
lit=set()
for _ in range(N):
    nap1=str(input()).strip()
    a,bc=nap1.split('+')
    b,c=bc.split('=')
    inputt.append((a,b,c))
    for el in a:
        lit.add(el)
    for el in b:
        lit.add(el)
    for el in c:
        lit.add(el)
literki=sorted(list(lit))
tabcyf=["1","2","3","4","5","6","7","8","9"]
guard2=True
def Permutacje(tab,inputt,l=0,tabk=[]):
    tabc=tab[:]
    if l==len(tab):
        global guard2
        guard=True
        for row in inputt:
            w1,w2,w3=row
            a=sklejacz(w1,tab)
            b=sklejacz(w2,tab)
            c=sklejacz(w3,tab)
            if a+b!=c:
                guard=False
                break
        if guard==True:
            print(sklejacz(literki,tab))
            guard2=False
            exit()
    for i in range(l,len(tab)):
        tabc[l],tabc[i]=tabc[i],tabc[l]
        Permutacje(tabc,inputt,l+1)

def sklejacz(a,tab):
    nap=''
    dictlit=dict(zip(["A","B","C","D","E","F","G","H","I"],tab))
    for el in a:
        nap+=dictlit[el]
    return int(nap)

Permutacje(tabcyf,inputt)
if guard2==True:
    print("BRAK")
end=time.time()
print(end-start)