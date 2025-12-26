#Program podający dzień tygodnia po dacie wiedząc że 1900 roku 1 stycznia był poniedziałek:

# rok przystępny musi dzielić się przez 4 ale nie przez 100 ale jeśli przez 400 to tak
# 1900 to nie rok przestępny
# prz 2025-1900=125 125//4 przestepnych - 125//100 - 125//400
# roków


def dztg(d,m,r) -> int: # w praktyce baza to 0.1.1900 ale nie ma takiego roku wiadomo
    rpb=1900//4-1900//100+1900//400
    rpf=r//4-r//100+r//400
    przys=rpf-rpb
    roz=r-1900
    l=przys+365*roz
    tab=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(m-1):
        l+=tab[i]
    l+=d
    if ((r%4==0 and r%100!=0) or r%400==0) and m<=2 and d<=29:
        l-=1

    return l%7 # 0 to niedziela

# mamy tablice stwierdzić ile jest trójkątów które są zdegenerowany (a+b<=c)
def zdegen(tab)->int:
    l=0
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            for k in range(j+1,len(tab)):
                if tab[i]+tab[j]<=tab[k] or tab[i]+tab[k]<=tab[j] or tab[k]+tab[j]<=tab[i]:
                    l+=1
                #end if
            #end for
        #end for
    #end for
    return l

# napis nazywamy wielkorotnym jeśli jest on jakimś napisem powielonym kilkukrotnie
def wielokrotny(nap)->int:
    max=0
    for i in range(len(nap)):
        for j in range(i+1,len(nap)):
            kan=nap[i:j]
            l=len(kan)
            nas=nap[i+l:j+l]
            if nas==kan:
                licz=0
                for k in range(i,len(nap),l):
                    if nap[k:k+l]==kan:
                        licz+=1
                    else:
                        break
                if licz>max:
                    max=licz
                    maxa=licz
    return maxa

print(wielokrotny('abcabcabcabck1kabcabck1kabcakkkkkkbcabclsjldhakjsdh'))

