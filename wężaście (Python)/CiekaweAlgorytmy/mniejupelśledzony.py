from math import sqrt
def Prime(a):
    if a<2:
        return 0
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return 0
    return 1

tabp=[]
for i1 in range(1,10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    for i6 in range(10):
                        if len(set([i1,i2,i3,i4,i5,i6]))==6:
                            nap=str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)
                            onap=nap[::-1]
                            tabp.append(nap+onap[1:])

for el in tabp[::-1]:
    if Prime(int(el))==1:
        print(el)