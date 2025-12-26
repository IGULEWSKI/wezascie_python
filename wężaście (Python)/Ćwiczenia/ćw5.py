n=4
def podzial(n:int,start=1,nap='')->None:
    if n==0 and ('+' in nap[:-1]):
        print(nap[:-1])
    for i in range(start,n+1):
        podzial(n-i,i,nap+str(i)+"+")


def zad161(n1,n2):
    samo=['a','e','o','i','u']
    def waga(n):
        nonlocal samo
        l=0
        suma=0
        for el in n:
            if el in samo:
                l+=1
            suma+=ord(el)
        return suma,l
    def wyraz(s1,s2)->bool:
        return rek(s2,waga(s1))

    def rek(s1,waga1,p=0,odp='')->bool:
        if p==len(s1):
            return waga(odp)==waga1
        return rek(s1,waga1,p+1,odp+s1[p]) or rek(s1,waga1,p+1,odp)# to jest genialne trzeba to zapisać to takie kombinatoryczne cudowne
    return wyraz(n1,n2)

def zad171(A,B)->int:
    l=0
    def Prime(a):
        if a<2:
            return False
        for i in range(a,a//2+1):
            if a%i==0:
                return False
        return True
    def rek(A:int,B:int,suma=1):
        nonlocal l
        if A==B==0 and Prime(suma)==False:
            l+=1
            return
        if A>0:
            rek(A-1,B,2*suma+1)
        if B>0:
            rek(A,B-1,2*suma)
    def fin(A,B)->int:#modre
        return rek(A-1,B)
    fin(A,B)
    return l
print(zad171(2,3))
    



    


    
    
    



     
    