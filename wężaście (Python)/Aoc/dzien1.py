#plik=open("dzien1.txt")
tab=[]
while True:
    try:
        a=input().strip()
        tab.append(a)
    except EOFError:
        break

poz=50 # aktualna pozycja
l=0
for el in tab: # jak jest R przed liczbą to dodajemy a jak L to odejmujemy a na końcu sprawdzamy czy aktualna pozycja jest == 0
    kier=el[0]
    war=int(el[1:])
    if kier=="R":
        poz+=war
    elif kier=="L":
        poz-=war
    poz=poz%100
    if poz==0:
        l+=1
print(l)
