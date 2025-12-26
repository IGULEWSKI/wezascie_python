def Silnia(a):
    s=1
    for i in range(2,a+1):
        s*=i
    return s
tab=[]
def Permutacje(tab,tabf=[]):
    if len(tabf)==len(tab):
        print(tabf)
    for el in tab:
        if el not in tabf:
            tabf.append(el)
            Permutacje(tab,tabf)
            tabf.pop()

    
Permutacje([1,2,3])