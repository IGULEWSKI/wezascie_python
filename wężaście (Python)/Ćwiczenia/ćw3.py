# deklaracja tablicy o roz N [0]*N
#T[i]
#len
#sito erastotenesa
from math import sqrt
def Sito(n) -> list:
    N=n+1
    tab=[1]*N
    tab[0]=0
    tab[1]=0
    for i in range(2,int(sqrt(N))+1):
        if tab[i]==1:
            for j in range(i*2,N,i):
                tab[j]=0
    return tab

# wypełniamy tablice losowymi liczbami spr czy w tej tablicy jest przynajmniej jedna cyfra nieparzysta

from random import randint

def f(N) -> bool:
    numbers=[0]*N
    for i in range(len(numbers)):
        numbers[i]=randint(0,222)
    for el in numbers:
            guard=False
            while el!=0:
                a=el%10
                if a%2==1:
                    guard=True
                el=el//10
            if guard == False:
                return False,numbers
    return True,numbers

# zamiana liczby na liczbe o podstawie k
def tab_size(n,k) -> int:
    x=1
    licz=0
    while n>x:
        x=x*k
        licz+=1
    return licz
#dowolny system liczbowy
def syst(n,k) -> list:
    size=tab_size(n,k)
    tab=[0]*size
    for i in range(size-1,-1,-1): # xd trzeba było while
        tab[i]=n%k
        n=n//k
    return tab

# dostajemy tablice i zwracamy ile bitów jest jedynkami


def bitowo(tab) -> int:
    licz=0
    for el in tab:
        while el!=0:
            a=el
            el=el>>1 # przekombinowane
            print(a,el)
            if a!=(el*2):
                licz+=1
    return licz

def xortab(tab) -> int:
    if len(tab)==0:
        return 0
    a=tab[0]
    for i in range(len(tab)):
        a=a^tab[i]
    return a
        

print(xortab([23,56,21]))