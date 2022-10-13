def get_randomList(firstnum, lastnum, darab=10, tizedesjegyekszama=0):
    import random
    x=[]
    for i in range(darab):
        rnd=random.uniform(firstnum,lastnum)
        rnd*=(10**tizedesjegyekszama)
        rnd=int(rnd)
        rnd=float(rnd)
        rnd/=(10**tizedesjegyekszama)
        x.append(rnd)
        # x.append(float(int(random.uniform(firstnum,lastnum)*(10**tizedesjegyekszama)))/(10**tizedesjegyekszama))
    return x

def Osszead(a,b):
    visszateresiertek=a+b
    return visszateresiertek

x=get_randomList(10,12,10,2)
print(x)


"""
s=0;
for i in range(len(X)):
    s+=X[i]
    
    """