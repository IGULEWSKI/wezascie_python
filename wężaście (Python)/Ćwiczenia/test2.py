a=(i**3 for i in range(10))
print(list(a))
def typy(*arg):
    print(type(arg))

typy(1,2,3)