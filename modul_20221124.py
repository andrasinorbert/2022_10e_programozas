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

def ptlan(x):
    return x%2==1

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