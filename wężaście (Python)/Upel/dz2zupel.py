from math import sqrt,factorial,pi,log,log10
def zad6(a) -> int:
    l=1
    suma=0
    while True:
        suma+=l
        l+=2
        if suma+l > a:
            return int(suma**0.5)
def zad7(N,r) -> int:
    a=N
    b=1
    for _ in range(r):
        a=(a+b)/2
        b=N/a
        print(a,b,N)
    return b
def zad8(N,r) -> int:
    a=N
    b=1
    c=1
    for _ in range(r):

        a=b=(a+b+c)/3
        c=N/(a*b)

    return b
def zad9(r=0.001) ->int:
    a=0
    b=5
    c=(a+b)/2
    g=c**c
    while abs(g-2024)>r:
        if g>2024:
            b=c
        else:
            a=c
        c=(a+b)/2
        print(a,b,c)
        g=c**c
    return b,g
def zad10(N)-> bool:
    a=1
    b=1
    for _ in range(N):
        if N==a*b:
            return True
        a,b=b,a+b

    return False
def zad11(a) -> bool:
    if a<2:
        return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return False
    return True
def zad12(a) -> list:
    tab=[]
    for i in range(1,a//2+1):
        if a%i==0:
            tab.append(i)
    tab.append(a)
    return tab

def zad13(a) -> list:
    i=2
    tab=[]
    while a>1:
        if a%i==0:
            a=a//i
            tab.append(i)
        else:
            i+=1
    return tab

def zad14(a) -> bool:
    if a==1:
        return True
    tab=zad12(a)
    tab.pop()
    print(tab)
    suma=0
    for el in tab:
        suma+=el
    if suma==a:
        return True
    return False
def zad14b(a) -> bool:
    suma=0
    for i in range(1,a//2+1):
        if a%i==0:
            suma+=i
        
    return suma
def zad15() -> list:
    tab=[]
    for i in range(1,1000000):
        c=zad14b(i)
        if c<1000000:
            tab.append((i,c))
    return tab
def zad16a(a,b) -> int:
    while a%b!=0:
        a,b=b,a%b
    return b
def zad16b(a,b,c) -> int:
    return zad16a(zad16a(a,b),c)
def zad17a(a,b):
    return a*b/zad16a(a,b)
def zad17b(a,b,c) -> int:
    return zad17a(zad17a(a,b),c)
def zad18(x,r) -> int:
    suma=0
    for n in range(r+1):
        suma+=((((-1)**n)/factorial(2*n))*(x**(2*n)))
    return suma
def zad19(r,l=sqrt(0.5)):
    print(l,r)
    if r==0:
        return l
    else: 
        return l*zad19(r-1,sqrt(0.5+0.5*l))
def zad20(a):
    l+=1
    while a!=1:
        return zad20(((a%2)*(3*a+1)+(1-a%2)*a/2))
def zad20f():
    min=99
    for i in range(2,101):
        l=0
        zad20(i)
        print(l)
        if l<min:
            min=l
            mina=i
    print(mina,min)

def zad21(N):
    l=0
    def zad21a(a):
        nonlocal l
        l+=1
        while a!=1:
            return zad21a(((a%2)*(3*a+1)+(1-a%2)*a/2))
    i=2
    while l!=N:
        l=0
        zad21a(i)
        i+=1
    return i-1
def zad22(n):
    def Fibo(n):
        a1=1
        a2=1
        for _ in range(n):
            a1,a2=a2,a1+a2
        return a2
    return Fibo(n)/Fibo(n+1)
def zad22lepiej(e)->int:
    a1=1
    a2=1
    x=0
    while abs(x-a2/a1)>e:
        x=a2/a1
        a1,a2=a2,a1+a2
    return x


def zad23(e)->int:
    i=0
    suma=0
    while True:
        suma+=1/factorial(i)
        i+=1
        if abs(suma-(suma+1/factorial(i)))<e:
            return suma
def zad25(n):
    def Prime(a):
        if a<2:
            return False
        for i in range(2,int(sqrt(a))+1):
            if a%i==0:
                return False
        return True
    def Palindrom(N): # nie działa można łatwo stringiem btw
        w=int(round(log(N,10),5))+1
        while w>1:
            p=N//(10**(w-1))
            k=N%10
            if p!=k:
                return False
            N=N%(10**(w-1))
            N=N//10
            if N!=0:
                w=int(round(log(N,10),5))+1
            else:
                w=0
        return True
        
            
    i=2
    for N in range(2,n):
        sN=N
        guard=True
        if Palindrom(N)==True:
            while N!=0:
                w=int(round(log(N,10),5))+1
                if Prime(N)==False:
                    guard=False
                    break
                N=N%(10**(w-1))
                N=N//10
            if guard==True:
                print(sN)
def zad19bezreku(n):
    a=sqrt(1/2)
    sum=1
    for _ in range(n+1):
        sum*=a
        a=sqrt(1/2+1/2*a)
    return 2/sum
def cosdziw(n):
    def rozk(n)->list:
        w=int(log10(n))+1
        tab=[0]*w
        l=0
        while n!=0:
            tab[w-l-1]=n%10
            l+=1
            n=n//10
        return tab
    def rozkbin(n,l):
        w=wielbin(l)
        tab=[0]*w
        l=-1
        for i in range(len(tab)-1,-1,-1):
            tab[i]=n%2
            n=n//2
        return tab
    def wielbin(n):
        l=0
        while n>0:
            n=n//2
            l+=1
        return l

    ncp=n
    w=int(log10(n))+1
    nap=rozk(n)
    licznik=0
    for i in range(1,2**len(nap)-1):
        mask=rozkbin(i,ncp)
        liczba=0
        for j in range(len(nap)):
            if mask[j]==1:
                liczba=liczba*10+nap[j]
        if liczba%7==0:
            licznik+=1
    return licznik
    # for i in range(1,2**w):

    #     print(i)
        
def wielbin(n):
    l=0
    while n>0:
        n=n//2
        l+=1
    return l
print(cosdziw(385))



