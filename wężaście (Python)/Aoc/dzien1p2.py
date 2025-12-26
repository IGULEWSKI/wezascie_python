plik=open("dzien1.txt")
poz=50 # aktualna pozycja
prevpoz=50
l=0
for el in plik:
    el=el.strip() # jak jest R przed liczbą to dodajemy a jak L to odejmujemy a na końcu sprawdzamy czy aktualna pozycja jest == 0
    kier=el[0]
    war=int(el[1:])
    if kier=="R":
        poz+=war
    elif kier=="L":
        poz-=war
    if poz>=100:
        l+=abs(poz)//100
    elif poz<=0 and prevpoz!=0:
        l+=(abs(poz)//100)+1
    elif poz<=0 and prevpoz==0:
        l+=(abs(poz)//100)
    if poz>=0:
        poz=poz%100
    else:
        cos=abs(poz)%100
        poz=100-cos
        poz=poz%100
    print(prevpoz,el,poz,l)
    prevpoz=poz
print(l)
