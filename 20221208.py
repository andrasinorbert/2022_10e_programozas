from typing import Iterable, Callable
input="Árvíztűrőtükörfúrógép"

def szetvalogatasTetele(lista:Iterable, func:Callable)->tuple:
    """
    Args:
        lista: list/string
        func: function return boolean
    Return:
        tuple[0]: when func is True
        tuple[1]: when func is False
    """
    c=0
    Y=[]
    Z=[]
    for i in range(len(lista)):
        if(func(lista[i])):
            c+=1
            Y.append(lista[i])
        else:
            Z.append(lista[i])
    return (Y,Z)

def maganhangzo_e(c):
    maganhangzok="aáeéiíoóöőuúüű"
    if(c.lower() in maganhangzok):
        return True
    return False
    # return True if c in maganhangzok else False

print(szetvalogatasTetele(input, maganhangzo_e))

def paros_e(szam):
    return szam%2==0

print(szetvalogatasTetele([2,3,4,5,6], paros_e))

def masolasTetel(lista, func):
    Y=[]
    
    return Y