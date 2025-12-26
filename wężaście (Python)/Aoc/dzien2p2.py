from sys import stdin
suma=0
def sprawdzacz(nap)->bool:# bruteforce spradzający dla każdego ciągu (spójnego z początkiem) znaków od początku do  maks połowy czy się powtarza do końca
    for i in range(1,len(nap)//2+1):
        pot=nap[0:i]
        guard=True
        if len(nap)%len(pot)==0:
            for j in range(0,len(nap),i):
                if nap[j:j+i]!=pot:
                    guard=False
                    break
            if guard==True:
                return True
    return False


for el in stdin.read().strip().split(','):
    a,b=el.split("-")
    a=int(a)
    b=int(b)
    for i in range(a,b+1):
        guard=True
        nap=str(i)
        if sprawdzacz(nap)==True:
            suma+=i
#podobnie co poprzednio ale przy pomocy sprawdzacza

print(suma)