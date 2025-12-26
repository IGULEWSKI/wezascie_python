plik=open("words.txt")
tab=[""]
dl=10
for linia in plik:
    a=linia.strip()
    for el in tab:
        if el in a and len(a)<dl:
            print(a)
    