from sys import stdin
suma=0
for el in stdin.read().strip().split(','):
    a,b=el.split("-")
    a=int(a)
    b=int(b)
    for i in range(a,b+1):
        nap=str(i)
        n=len(nap)
        if n%2==0:
            pol=n//2
            p1=nap[0:pol]
            p2=nap[pol:]
            if p1==p2:
                suma+=i
print(suma)
"""dzieli każdy element
w zakresie a-b na pół i sprawdz 
czy te połówki są identyczne"""
