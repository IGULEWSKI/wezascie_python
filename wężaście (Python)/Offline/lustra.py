from copy import deepcopy
tab=[]
N,L=map(int,input().split(' '))
ogrod=[[None for _ in range(N)] for _ in range(N)]
for _ in range(L):
    w,k,kat=tuple(map(int,input().split(' ')))
    tab.append((w,k,kat))
    ogrod[w][k]=kat
# tab=[(0, 4, 45), (1, 1, 45), (3, 0, 135), (3, 3, 45), (4, 1, 135), (4, 4, 135)]
# N=5
# L=6
def check(ogrod,Nw,tab):
    sl=0 #status lasera czyli leci w dol dol-0 gora-1 prawo-2 lewo-3
    ogrod2=[[0 for _ in range(N)] for _ in range(N)]
    keys=[(el[0],el[1]) for el in tab]
    values=[False for _ in range(len(tab))]
    slo=dict(zip(keys,values))
    w=0
    k=0
    w1=Nw-1
    k1=Nw-1
    sl1=1
    guard=True
    guard1=True
    while guard==True or guard1==True:
        if guard==True:
            if ogrod[w][k]==45:
                slo[(w,k)]=True
                if sl==0: sl=3
                elif sl==1: sl=2
                elif sl==3: sl=0
                elif sl==2: sl=1
                if ogrod2[w][k]>0:
                    guard=False
            elif ogrod[w][k]==135:
                slo[(w,k)]=True
                if sl==0: sl=2
                elif sl==1: sl=3
                elif sl==3: sl=1
                elif sl==2: sl=0
                if ogrod2[w][k]>0:
                    guard=False
            ogrod2[w][k]+=1
            if ogrod2[w][k]==2:
                ost=(w,k)
                war=list(slo.values())
                if war.count(False)==0:
                    return (w,k)
            if sl==0: w+=1
            elif sl==1: w-=1
            elif sl==2: k+=1
            elif sl==3: k-=1
            if w<0 or k<0 or w>Nw-1 or k>Nw-1:
                guard=False
        if guard1==True:
            if ogrod[w1][k1]==45:
                slo[(w1,k1)]=True
                if sl1==0: sl1=3
                elif sl1==1: sl1=2
                elif sl1==3: sl1=0
                elif sl1==2: sl1=1
                if ogrod2[w1][k1]>0:
                    guard1=False
            elif ogrod[w1][k1]==135:
                slo[(w1,k1)]=True
                if sl1==0: sl1=2
                elif sl1==1: sl1=3
                elif sl1==3: sl1=1
                elif sl1==2: sl1=0
                if ogrod2[w1][k1]>0:
                    guard1=False   
            ogrod2[w1][k1]+=1
            if ogrod2[w1][k1]==2:
                ost=(w1,k1)
                war=list(slo.values())
                if war.count(False)==0:
                    return (w1,k1)
            if sl1==0: w1+=1
            elif sl1==1: w1-=1
            elif sl1==2: k1+=1
            elif sl1==3: k1-=1
            if w1<0 or k1<0 or w1>Nw-1 or k1>Nw-1:
                guard1=False
    war=list(slo.values())
    if war.count(False)==0:
        klu=list(slo.keys())
        return ost
    return False
def fin(ogrod,tab,N):
    for el in tab:
        copy=tab[:]
        copy.remove(el)
        wf=el[0]
        kf=el[1]
        katf=el[2]
        ogrod[wf][kf]=None
        pot=check(ogrod,N,tab)
        if pot!=False:
            return pot,(wf,kf)
        ogrod[wf][kf]=katf
# def brucik(ogrod,tab,N):
#     for i in range(len(tab)):
#         wf=tab[i][0]
#         kf=tab[i][1]
#         katf=tab[i][2]
#         ogrod[wf][kf]=None
#         pot=check(ogrod,N,tab,wf,kf)
#         ogrod[wf][kf]=katf
#         if pot!=False:
#             return ((wf,kf),pot)


b=fin(ogrod,tab,N)
print(b)

