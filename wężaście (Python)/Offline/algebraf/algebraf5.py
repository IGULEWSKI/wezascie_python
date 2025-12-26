N=int(input())                                                                  
inputt=[]                                                                       
lit=set()
guard2=False                                                                      
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
    if len(c) > max(len(a)+1,len(b)+1) or len(c)<max(len(a),len(b)):
        guard2=True
if guard2==True:
    print("BRAK")
    exit()                                                     
literki=sorted(list(lit))                                                       
tabcyf=["1","2","3","4","5","6","7","8","9"]                                    
guard2=True                                                                     
def Permutacje(tab,inputt,l=0,tabk=[]):                                         
    tabc=tab[:]                                                                 
    if l==len(tab):                                                                                                                      
        guard=True                                                              
        for row in inputt:                                                      
            w1,w2,w3=row                                                        
            a=sklejacz(w1,tab)                                                  
            b=sklejacz(w2,tab)                                                  
            c=sklejacz(w3,tab)                                                  
            if a+b!=c:                                                          
                guard=False                                                     
                break                                                           
        if guard==True:                                                         
            print(sklejacz(literki,tab))                                                                                             
            exit()                                                              
    for i in range(l,len(tab)):                                                 
        tabc[l],tabc[i]=tabc[i],tabc[l]                                         
        Permutacje(tabc,inputt,l+1)                                             
                                                                                
def sklejacz(a,tab):                                                            
    nap=''                                                                      
    dictlit={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8}             
    for el in a:                                                                
        nap+=tab[dictlit[el]]                                                   
    return int(nap)                                                                                                                                         
Permutacje(tabcyf,inputt)                                                                                                                      
print("BRAK") 