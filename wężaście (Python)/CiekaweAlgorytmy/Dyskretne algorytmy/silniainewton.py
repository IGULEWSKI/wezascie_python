def silnia(n):
    ilo=1
    for i in range(2,n+1):
        ilo*=i
    return ilo
def newton(n,k):
    if k>n:
        return 0
    return silnia(n)/(silnia(k)*silnia(n-k))

suma=0
for i in range(0,4):
    suma=suma+((-1)**i)*newton(7,i)*((newton(7-i,3))**7)
