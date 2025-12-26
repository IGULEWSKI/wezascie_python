napis=input().strip()
def zad(nap):
    V=["A","E","I","O","U","Y"]
    def mnozenie(a,b):
        if a in V and b in V:
            return chr(max(ord(a),ord(b)))
        elif a in V and b not in V:
            return b
        elif a not in V and b in V:
            return a
        else:
            return chr(min(ord(a),ord(b)))
    def dodawanie(a,b):
        if a in V and b in V:
            return chr(min(ord(a),ord(b)))
        elif a in V and b not in V:
            return a
        elif a not in V and b in V:
            return b
        else:
            return chr(max(ord(a),ord(b)))
    def wyraz(nap:str)->str:
        if len(nap)==1:
            return nap
        guard=False
        pocz=None
        kon=None
        for i in range(len(nap)):
            if nap[i]=='(':
                pocz=i
                guard=True
            if guard==True and nap[i]==')':
                kon=i
            if pocz!=None and kon!=None:
                podwyr=nap[pocz+1:kon]
                fin=wyraz(podwyr)
                return wyraz(nap[:pocz]+fin+nap[kon+1:])
        for i in range(len(nap)):
            if nap[i]=='*':
                a=nap[i-1]
                b=nap[i+1]
                podwyr=mnozenie(a,b)
                return wyraz(nap[:i-1]+podwyr+nap[i+2:])
        for i in range(len(nap)):
            if nap[i]=='+':
                a=nap[i-1]
                b=nap[i+1]
                podwyr=dodawanie(a,b)
                return wyraz(nap[:i-1]+podwyr+nap[i+2:])
    return wyraz(nap)
print(zad(napis))




