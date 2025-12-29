N=int(input())
tab=list(map(int,input().split(' ')))
# N=10
# tab=[2, 0, 3, 0, 3, 0, 3, 0, 0, 1]
if sum(tab)<N-1:
    print("BRAK")
    exit(0)
def skoczek(tab,N,p=0,E=0,licz=0):
    E+=tab[p]
    if E+1<N-p:
        for i in range(E,0,-1):
            skoczek(tab,N,p+i,E-i,licz+1)
    else:
        print(licz+1)
        exit(0)
skoczek(tab,N)
print("BRAK")