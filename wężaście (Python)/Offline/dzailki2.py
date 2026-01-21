N=int(input())
tab = [int(input()) for _ in range(N)] #to działa xd
SP = [None for _ in range(N)]
#Za wolmo to próbujemy to do tego podejść inaczej
def zad(tab,SP):
    guard=True
    def kupowacz(tab,SP): #kupuje oczywiste punkty
        while None in SP:
            i=0
            SP1=SP[:]
            while i<len(tab):
                if i-1<0:
                    if tab[i]>=tab[i+1]:
                        SP[i]=tab[i]
                        SP[i+1]=0
                        tab[i+1]=0
                        i+=1
                elif i+1>N-1:
                    if tab[i]>=tab[i-1]:
                        SP[i]=tab[i]
                        tab[i-1]=0
                        SP[i-1]=0
                else:
                    if tab[i]>=tab[i+1]+tab[i-1]:
                        SP[i]=tab[i]
                        tab[i+1]=0
                        tab[i-1]=0
                        SP[i-1]=0
                        SP[i+1]=0
                        i+=1
                i+=1
            if SP1==SP:
                nonlocal guard
                guard=False
                break
    kupowacz(tab,SP)
    if guard==True:
        print(sum(SP))
        exit(0)
    SPNP=SP[:]
    SPP=SP[:]
    i=0
    while i<len(tab):
        if SPNP[i]==None:
            SPNP[i]=tab[i]
            if i+1<N:
                SPNP[i+1]=0
        if i+1<N:
            if SPP[i+1]==None and SPP[i]==None:
                SPP[i+1]=tab[i+1]
                SPP[i]=0
        elif SPP[i]==None:
            if SPP[i-1]==0:
                SPP[i]=tab[i]
            else:
                SPP[i]=0

        i+=2
    print(max(sum(SPP),sum(SPNP)))

    

zad(tab,SP)
