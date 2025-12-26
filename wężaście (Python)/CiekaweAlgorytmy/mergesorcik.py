tab=[3,1,7,4,43242,-15,8,13,2]

def merge(tab1,tab2):
    fin=[0]*(len(tab1)+len(tab2))
    pointer1=0
    pointer2=0
    l=0
    while pointer1<=len(tab1)-1 or pointer2<=len(tab2)-1:
        if pointer1>len(tab1)-1:
            fin[l]=tab2[pointer2]
            pointer2+=1
        elif pointer2>len(tab2)-1:
            fin[l]=tab1[pointer1]
            pointer1+=1
        elif tab1[pointer1]>tab2[pointer2]:
            fin[l]=tab1[pointer1]
            pointer1+=1
        else:
            fin[l]=tab2[pointer2]
            pointer2+=1
        l+=1
    return fin
def mergesort(tab):
    pol=len(tab)//2
    if len(tab)==1:
        return tab
    return merge(mergesort(tab[0:pol]),mergesort(tab[pol:]))
print(mergesort(tab))