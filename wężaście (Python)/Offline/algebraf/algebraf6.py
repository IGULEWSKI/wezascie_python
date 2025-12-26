from itertools import combinations
N=int(input())                                                                  
inputt=[]                                                                       
lit=set()                                                                       
for _ in range(N):                                                              
    nap1=str(input())                                                         
    a,bc=nap1.split('+')                                                        
    b,c=bc.split('=')                                                           
    inputt.append((a,b,c))                                                      
    for el in a:                                                                
        lit.add(el)                                                             
    for el in b:                                                                
        lit.add(el)                                                             
    for el in c:                                                                
        lit.add(el)                                                             
literki=sorted(list(lit))                                                       
tabcyf=["1","2","3","4","5","6","7","8","9"]
kombinacje=list(combinations(tabcyf,len(literki)))                                
guard2=True   
def Permutacje(tab,inputt,l=0):
    tab=list(tab)                                         
    tabc=tab[:]                                                                 
    if l==len(tab):                                                             
        global guard2
        global literki
        dictlit=dict(zip(literki,tab))
        guard=True                                                              
        for row in inputt:                                                      
            w1,w2,w3=row                                                        
            a=sklejacz(w1,dictlit)                                                  
            b=sklejacz(w2,dictlit)                                                  
            c=sklejacz(w3,dictlit)                                                  
            if a+b!=c:                                                          
                guard=False                                                     
                break                                                           
        if guard==True:                                                         
            print(sklejacz(literki,dictlit))                                        
            guard2=False                                                        
            exit()                                                              
    for i in range(l,len(tab)):                                                 
        tabc[l],tabc[i]=tabc[i],tabc[l]                                         
        Permutacje(tabc,inputt,l+1)                                             
                                                                                
def sklejacz(a,dictlit):                                                            
    nap=''                                                                                 
    for el in a:                                                                
        nap+=dictlit[el]                                             
    return int(nap)                                                             
for el in kombinacje:                                                                          
    Permutacje(el,inputt)                                                       
if guard2==True:                                                                
    print("BRAK")                                                               