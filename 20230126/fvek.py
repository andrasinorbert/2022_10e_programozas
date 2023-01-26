

def szamtani(lista):
    osszeg=0
    db=len(lista)
    
    #for i in lista:
    #    osszeg+=i
    
    for i in range(len(lista)):
        osszeg+= lista[i]
        
    print(osszeg/db)
    
def szamtani2(lista):
    return sum(lista)/len(lista)

def mertani(lista):
    szorzat=1
    
    for i in range(len(lista)):
        szorzat*= lista[i]
    
    #n-edik = 1/n hatvány
    return szorzat**(1/len(lista))

    