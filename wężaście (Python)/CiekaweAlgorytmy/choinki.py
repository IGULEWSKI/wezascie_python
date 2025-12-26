n=6
for i in range(1,n+1):
    spa=n-i
    licz=i*2-1
    while licz>0 or spa>0:
        if spa>0:
            print(" ",end="")
            spa-=1
        elif licz>0:
            print("*",end="")
            licz-=1
    print()
    
