tab=[1,3,4,16,24]

def waga(tab,suma,tabf=[],zb=set()):
    tab=tab[:]
    if suma==0:
        zb.add(tuple(tabf))
    elif suma>0 and len(tab)>0:
        odw=tab[-1]
        tab.pop()
        waga(tab,suma-odw,tabf+[odw])
        waga(tab,suma,tabf)
    return zb
def wagazwyk(tab,n,p=0):
    if n==0:
        return True
    if p<len(tab) and n>0:
        return wagazwyk(tab,n-tab[p],p+1) or wagazwyk(tab,n,p+1) or wagazwyk(tab,n+tab[p],p+1) # drzewo trinarne
    return False
print(waga(tab,18),wagazwyk(tab,18))

