def zad1(N) -> set:
    tab=[]
    for i in range(1,N-1):
        for j in range(i+1,N):
            for k in range(j+1,N+1):
                if i**2 + j**2 ==k**2 and j+i>k:
                    tab.append((i,j,k))
                    
    return tab
def zad2():
    cyfry=["0","1","2","3","4","5","6","7","8","9"]
    for el1 in cyfry:
        for el2 in cyfry:
            for el3 in cyfry:
                if el1!="0" and el2!="0":
                    abc=int(el1+el2+el3)                
                    bbb=int(el2+el2+el2)
                    if abc+abc+abc==bbb:
                        return el1,el2,el3
def zad3():
    an=0
    an1=1
    print(an)
    print(an1)
    while an1<1000000:
        print(an1)
        an2=an+an1
        an1,an=an2,an1

def zad4():
    for i in range(1020):
        for j in range(i+1,1020):
            an=i
            an1=j
            while an1<=2025:
                if an1==2025:
                    return i,j
                an2=an+an1
                an1,an=an2,an1
def zad5(n):
    an=0
    an1=1
    tab=[an]
    while an1<n:
        tab.append(an1)
        an2=an+an1
        an1,an=an2,an1
    for j in range(len(tab)):
        suma=0
        for i in range(j,len(tab)):
            suma+=tab[i]
            if suma==n:
                return True
    return False


