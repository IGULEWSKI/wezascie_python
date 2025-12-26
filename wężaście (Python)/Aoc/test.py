# a='123'
# print(a[-1])
# def dek(*a):
#     print(a)
# dek(2,3,4)
# tab=[1,2,3,4,5,6]
# print(*tab)
# k='123'
# nap='1234123'
# for j in range(len(nap)):
#     print(k[j%len(k)],nap[j]) # sprawdzam czy nap zapętla znaleziony klucz
#     if k[j%len(k)]!=nap[j]:
#         guard=False
#         break
def sprawdzacz(nap):
    for i in range(1,len(nap)//2+1):
        pot=nap[0:i]
        guard=True
        if len(nap)%len(pot)==0:
            for j in range(0,len(nap),i):
                print(pot,nap[j:j+i])
                if nap[j:j+i]!=pot:
                    guard=False
                    break
            if guard==True:
                return True
    return False

print(sprawdzacz("267267997"))