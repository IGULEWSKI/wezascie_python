plik=open('dzien3.txt')
def wybnaj(tab:list,n,start=0,nap=''):
    max=0
    if n==0:
        return int(nap)
    else:
        for i in range(start,len(tab)-(n-1)):
            if tab[i]==9:
                return wybnaj(tab,n-1,i+1,nap+'9')
            if tab[i]>max:
                max=tab[i]
                ii=i
        return wybnaj(tab,n-1,ii+1,nap+str(max))

suma=0
for linia in plik:
    nap=linia.strip()
    tab=list(map(int,list(nap)))
    suma+=wybnaj(tab,12)
print(suma)
        
        


        


