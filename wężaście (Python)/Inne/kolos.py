from copy import deepcopy
def gencz(a):
    i=2
    while a>1:
        if a%i==0:
            a=a//i 
            yield i
        else:
            i+=1



tab=[12,6,6,26,15,15,3]
wyn=[]
N=len(tab)
def zad2(tab,start,p=0,i=-1,najm=11):
    if p==0:
        i=start
        najm=11
    elif i==start:
        return p
    if p==10:
        return 10
    for el in gencz(tab[i]):
        if el<tab[i]:
            if tab[i]%2==0:
                if i+el<N:
                    najm=min(zad2(tab,start,p+1,i+el),najm)
            if tab[i]%2==1:
                if i-el>=0:
                    najm=min(zad2(tab,start,p+1,i-el),najm)
    return najm

sudo=['534678912', '672195348', '198342567', '859761423', '426853791', '713924856', '961537284', '287419635', '345286179']
def sprawdzacz(tab):
    kol=[[tab[j][i] for j in range(len(tab))] for i in range(len(tab))]
    for i in range(len(tab)):
        if len(set(tab[i]))==9:
            if len(set(kol[i]))==9:
                continue
        return False
    return True

def zamieniacz(tab):
    wyn=[[],[],[],[],[],[],[],[],[]]
    for i in range(len(tab)):
        k=(i//3)*3
        for j in range(0,9,3):
            mal=tab[i][j:j+3]
            wyn[k].append(mal)
            k+=1
    return wyn
def odwzam(tab):
    wyn=["","","","","","","","",""]
    for i in range(len(tab)):
        k=(i//3)*3
        for j in range(len(tab[0])):
            wyn[k]+=tab[i][j]
            k+=1
    return wyn

def sudobrute(sudotab):
    for i in range(len(sudotab)):
        for j in range(len(sudotab)):
            if i==j:
                continue
            nowytab=deepcopy(sudotab)
            nowytab[i],nowytab[j]=nowytab[j],nowytab[i]
            if sprawdzacz(odwzam(nowytab))==True:
                return (i+1,j+1)
    return "Było git"
zamsudo=zamieniacz(sudo)
print(odwzam(zamsudo)==sudo)
zamsudo[0],zamsudo[3]=zamsudo[3],zamsudo[0]
sudo2=odwzam(zamsudo)
print(sudobrute(zamieniacz(sudo2)))


