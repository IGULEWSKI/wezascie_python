from math import log,log10
def NWD(a,b) -> int:
    while b!=0:
        a,b=b,a%b
    return a
def NWD3(a,b,c) ->int:
    return NWD(NWD(a,b),c)
def NWW(a,b) -> int:
    return a*b//NWD(a,b)
def NWW3(a,b,c) -> int:
    return NWW(a,b)*c//NWD(NWW(a,b),c)
def cary(a) -> bool:
    if a<100:
        return True
    a1=a%10
    a=a//10
    a2=a%10
    a=a//10
    q=a2/a1
    while a!=0:
        a3=a%10
        if a2==0 or a3==0:
            return False
        if a3/a2!=q:
            return False
        a2=a3
        a=a//10
    return True

def FiboSuma(n):
    Fibo=[1,1,2,3,5,8,13,21]
    for i in range(len(Fibo)-1):
        suma=0
        for j in range(i,len(Fibo)-1):
            suma+=Fibo[j]
        if suma==n:
            return True
    return False
    
    
    return False

def Fibo2(n) -> bool:
    Fibo=[1,1,2,3,5,8,13,21]
    l=1
    while Fibo[l]<n:
        suma=0
        r=l
        while suma<n:
            suma+=Fibo[r]
            r+=1
        if suma==n:
            return True
        l+=1
    return False


def czy_wnik(n) -> bool:
    l=0
    c=n
    while c>0:
        c=c//10
        l+=1
    a=n
    b=n
    for i in range(l):
        a1=a%10
        b=n
        for j in range(l):
            if i==j: 
                b=b//10
            else:
                b1=b%10
                b=b//10
                if a1==b1:
                    return False
        a=a//10
    return True
def genialneuni(n):
    x=0
    while n>0:
        if x==x|(1<<(n%10)):
            return False
        x=x|(1<<(n%10))
        print(bin(x))
        n//=10
    return True
# | or
# ^ xor
# & and
# << left bitshift przesuwa binarke w lewo o n (bin<<n)
# >> right bitshift