def Permutacje1(n):
    n.append("|")
    stack=[n]
    odp=[]
    while len(stack)>0:
        a=stack.pop()
        if a[0]=="|":
            tab=a[1:]
        else:
            for i in range(len(a)):
                if a[i]!="|":
                    b=a[:]
                    c=b.pop(i)
                    b.append(c)
                    stack.append(b)
                else:
                    break
print(Permutacje1([1,2,3,4,5,6,7,8,9]))
