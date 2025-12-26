from math import factorial
def skoczek(N):
    def możliwe(T,w,k,i):
        dw=(-2,-1,1,2,2,1,-1,-2)
        dk=(1,2,2,1,-1,-2,-2,-1)
        nw=w+dw[i]
        nk=k+dk[i]
        if nw>=0 and nw<=N-1 and nk>=0 and nk<=N-1 and T[nw][nk]==0:
            return nw,nk
        return (-1,-1)
    def czyniema0(tab):
        for i in range(N):
            if 0 in tab[i]:
                return False
        return True
    def Wypisz(tab):
        for i in range(N):
            for j in range(N):
                print(f"{tab[i][j]:4}",end='')
            print()
        print()
    roz=N*N
    tabo= [[0 for _ in range(N)] for _ in range(N)]
    def skoczekrek(tab=tabo,r=1,w=0,k=0):
        tab[w][k]=r
        if r==roz:
            if czyniema0:
                Wypisz(tab)
        else:
            for i in range(8):
                nw,nk=możliwe(tab,w,k,i)
                if nw!=-1:
                    skoczekrek(tab,r+1,nw,nk)
        tab[w][k]=0 # robimy tak bo działamy ciągle na adresie tablicy
    skoczekrek()
def palizad(a,b):
    if a%2==0:
        a=a-1
    elif b%2==0:
        b=b-1
    k1=a//2
    k2=b//2
    return factorial(k1+k2)//factorial(k1)*factorial(k2)
def 
print(palizad(5,8))

            

        