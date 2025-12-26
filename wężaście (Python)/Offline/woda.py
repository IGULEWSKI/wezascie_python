from time import sleep
N=4
tab=[20,12,7,4]
def fin(maxpoj,N):
    act=[0 for _ in range(N)]
    act[0]=maxpoj[0]
    if len(maxpoj)==2 and 1 not in tab:
        return "BRAK"
    mwar=min(maxpoj)
    mini=maxpoj.index(mwar)

    np=[]
    for i in range(0,N):
        if tab[i]%2==1:
            np.append((tab[i],i))
    if len(np)==0:
        return "BRAK"
    mnpwar,mininp=sorted(np,key=lambda x: x[0])[0]
    if mini==0 and maxpoj[0]!=1:
        return "BRAK"
    elif mini==0 and maxpoj[0]==1:
        return 0
    elif 1 in maxpoj:
        return 1
    print(mnpwar,mininp,mwar,mini)
    l=0
    if mininp!=mini and maxpoj[mininp]-maxpoj[mini]>maxpoj[mini]:
        while 1 not in act:
            act[0]-=mwar
            l+=mwar
            act[mininp]+=mwar
            if act[mininp]<=maxpoj[mininp]:
                l+=mwar
            else:
                roz=act[mininp]%maxpoj[mininp]
                act[mininp]=maxpoj[mininp]
                l+=roz
                act[mini]=roz
            sleep(0.5)
            print(act,l)
    elif mininp!=mini and maxpoj[mininp]-maxpoj[mini]<=maxpoj[mini]:
        while 1 not in act:
            act[0]-=mnpwar
            l+=mnpwar
            roz=mnpwar%mwar
            act[mininp]=roz
            act[mini]+=mwar
            l+=mwar
            sleep(0.5)
            print(act,l)
    return l

            






print(fin(tab,N))