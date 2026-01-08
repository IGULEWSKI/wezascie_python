N=int(input())
tab = [int(input()) for _ in range(N)] #to działa xd
SP = [None for _ in range(N)]
wyn=[]
def zad(tab,SP,i=0):
    global wyn
    if i==N:
        wyn.append(sum(SP))
    else:
        SPK1=SP[:]
        SPK2=SP[:]
        SPK1[i]=tab[i]
        if i+1<=N-1:
            SPK1[i+1]=False
            zad(tab,SPK1,i+2)
            SPK2[i]=False
            zad(tab,SPK2,i+1)
        else:
            zad(tab,SPK1,i+1)
zad(tab,SP)
print(max(wyn),wyn)