N=int(input())
tab = [int(input()) for _ in range(N)]
zysk = [None for _ in range(N)]
zysk[0]=tab[0]
zysk[1]=max(zysk[0],tab[1])

for i in range(2,N):
    zysk[i]=max(zysk[i-1],zysk[i-2]+tab[i]) # sprawdzamy czy bardziej się opłaca wziąć działkę pomiędzy czy odpuścic tą działkę
print(zysk[-1])

