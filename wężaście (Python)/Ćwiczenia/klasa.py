class BNode:
    def __init__(self):
        self.val=None #int
        self.left=None #BNode
        self.right=None #BNode
root= BNode()
root.val=3
right=BNode()
right.val=7
left=BNode()
left.val=8
root.right=right
root.left=left
def f(root:BNode) -> int:
    if root.left ==None and root.right==None:
        return root.val
    L=0
    if root.left is not None:
        L=f(root.left)
    R=0
    if root.right!=None:
        r=f(root.right)
    return root.val + L + R
def iter(root:BNode,n):
    tab=[0]*n
    suma=0
    tab[0]=root
    for i in range(n-2):
        if tab[i]!=0:
            suma+=tab[i].val
        if root.left is not None:
            tab[i+1]=root.left
        if root.right is not None:
            tab[i+2]=root.right
        i+=2
    if tab[-1]!=0:
        suma+=tab[-1].val
    if tab[-2]!=0:
        suma+=tab[-2].val

    return suma



    
# def merge(t1,t2) -> list[int]:
#     res=[0]*(len(t1)+len(t2))
#     pointer1=0
#     pointer2=0
#     for i in range(len(res)):
#         if pointer1>=len(t1):
#             res[i]=t2[pointer2]
#             pointer2+=1
#         elif pointer2>=len(t2):
#             res[i]=t1[pointer1]
#             pointer1+=1
#         elif t1[pointer1]>t2[pointer2]:


def nsum(T,S,n=3,start=0):
    if n==0: return S==0
    for i in range(start,len(T)):
        nexta=nsum(T,S-T[i],n-1,i+1)
        if nexta==True: return True
    return False


T=[2,18,3,4,1,2,1,1,1,1,1]
print(nsum(T,31,6))
    


