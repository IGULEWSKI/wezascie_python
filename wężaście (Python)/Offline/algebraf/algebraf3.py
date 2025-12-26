N=int(input())
inputt=[]
lit=set()
for _ in range(N):
    nap1=str(input())
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
def Permutacje1(n,inputt):
    n.append("|")
    stack=[n]
    odp=[]
    while len(stack)>0:
        a=stack.pop()
        if a[0]=="|":
            tab=a[1:]
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
        else:
            for i in range(len(a)):
                if a[i]!="|":
                    b=a[:]
                    c=b.pop(i)
                    b.append(c)
                    stack.append(b)
                else:
                    break

def sklejacz(a,tab):
    nap=''
    dictlit={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8}
    for el in a:
        nap+=tab[dictlit[el]]
    return int(nap)

Permutacje1(tabcyf,inputt)
if guard2==True:
    print("BRAK")



"""
3
ABC+DEF=EGH
BCF+FBH=IFE
AAA+BBB=CCC

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
"""