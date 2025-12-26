N=int(input())
tab=list(map(int,input().strip().split(' ')))
NP = [el for el in tab if el%2==1]
def fin(tab,NP):
    mini=min(tab)
    wyn=[]
    start=tab[0]
    if len(NP)==0:
        return "BRAK"
    if 1 in tab:
        return 0
    if start==mini and mini!=1:
        return "BRAK"
    if mini==1 and start!=mini:
        return 1
    if start==mini and mini==1:
        return 0
    if tab[0]%2==1 and sum(tab[1:])>tab[0]:
        y=tab[0]
        for x in tab:
            if (y-1)%x==0:
                wyn.append(((((y-1)//x)*2)-1)*x)
        NP.pop(0)
    for k in range(1,len(tab)):
        for m in range(k,len(tab)+1):
            if k==m: continue
            else:
                pot=tab[k:m]
                if sum(pot)==start-1:
                    wyn.append(start-1)
    for i in range(len(tab)):
        x=tab[i]
        for j in range(len(NP)):
            y=NP[j]
            if i==j:
                continue
            else:
                if (y+1)%x==0:
                    wyn.append((((y+1)//x)*2*x)-1)
                if (y-1)%x==0:
                    wyn.append(y+((((y-1)//x)*2)-1)*x)
                if (x+1)%y==0:
                    wyn.append((((x+1)//y)*2*y)-1)
    if len(wyn)>0:
        return min(wyn)
    else:
        return "BRAK"
print(fin(tab,NP))