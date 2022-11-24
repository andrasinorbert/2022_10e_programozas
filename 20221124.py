
def kiir(x):
    print(x)
    
kiir(3)
kiir("szia")
kiir([3,4,5])
kiir((4,5))

def OsszegzesTetel(X):
    s=0
    for i in range(len(X)):
        s+= X[i]
    return s
        
c=OsszegzesTetel([3,4,5])
print(c)
print(OsszegzesTetel([3,4,5]))

def osszead(x,y):
    return x+y

def paros(x):
    return x%2==0

def megszamolasTetel(X, func):
    c=0
    for i in range(len(X)):
        if func(X[i]):
            c+=1
    return c

print(megszamolasTetel([2,3,4,5], paros))

def ptlan(x):
    return x%2==1
print(megszamolasTetel([2,3,4,5], ptlan))

# min-max keresés
def szelsoErtekKereses(X, func):
    index=0
    szelsoErtek=X[0]
    for i in range(1,len(X)):
        if( func(szelsoErtek, X[i]) ):
            index=i
            szelsoErtek=X[i]
    return (index, szelsoErtek)
def kisebb(a,b):
    return a<b if True else False
def nagyobb(a,b):
    return a>b if True else False
print(f"max: {szelsoErtekKereses([3,4,5,2], kisebb)}")
print(f"min: {szelsoErtekKereses([3,4,5,2], nagyobb)}")