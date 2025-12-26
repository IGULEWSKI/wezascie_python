import time
def newton(n,k) -> int:
    if k==1:
        return n
    elif k==0:
        return 1
    elif k==n:
        return 1
    elif k==n-1:
        return n
    elif n<k:
        return 0
    else:
        return newton(n-1,k-1) + newton(n-1,k)
tabf=[0]*9999
i=0
def krol(w,k,tab,suma=0):
    if w>7:
        global tabf
        global i
        tabf[i]=suma
        i+=1
    else:
        suma+=tab[w][k]
        if k==0:
            krol(w+1,k,tab,suma)
            krol(w+1,k+1,tab,suma)
        elif k==7:
            krol(w+1,k,tab,suma)
            krol(w+1,k-1,tab,suma)
        else:
            krol(w+1,k-1,tab,suma)
            krol(w+1,k,tab,suma)
            krol(w+1,k+1,tab,suma)
def fibo(n) -> int:
    T=[-1*(n+1)]
    def sub_fibo(k):
        nonlocal T
        if T[k]!=-1:
            return T[k]
        if k<2:
            return k
        fib_k = sub_fibo(k-1)+sub_fibo(k-2)
        tab[k]=fib_k
        return fib_k
    return sub_fibo(n)


start=time.time()
tab=[[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8],[2,3,4,5,6,23,1,8]]
krol(0,4,tab)
print(max(tabf))
end=time.time()
print(end-start)
print(fibo(3))