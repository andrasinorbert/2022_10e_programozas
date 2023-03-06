"""
Írjon függvényt adatokBeolvasása néven, amelyik beolvassa a fájl tartalmát egy megfe-
lelő adatszerkezetbe! Ügyeljen arra, hogy a havi futásteljesítmények numerikus értékekként
legyenek eltárolva az Ön által választott adatszerkezetben!
"""
rendszamok=[]
kmek=[]

def adatokBeolvasasa():
    f=open("20230302/input.txt", "r", encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    #print(sorok)
    
    for i in range(len(sorok)):
        egysor=sorok[i].strip()
        egysor_l=egysor.split(" ")
        rendszamok.append(egysor_l[0])
        tmp=[]
        for j in range(1,len(egysor_l)):
            tmp.append(int(egysor_l[j]))
        kmek.append(tmp)
        
adatokBeolvasasa()

print(rendszamok)
print(kmek)

"""
Írjon függvényt nullaKm néven,
    amely visszaadja a hívás helyére,
    hogy hány olyan hónap volt
2021-ben a teljes adathalmazban,
    amikor egy teherautó egy hónapban
    nulla km-t tett meg! A
nullaKm függvény által visszaküldött darabszám
    értéket a főprogramban írja ki a példában
látható módon!
Az alábbi példa a program egy lehetséges futási eredményét mutatja:
Az adatbázisban 29 db 0 km havi futásteljesítményt tartalmazó hónap van.
"""

def nullaKm():
    c=0
    for i in kmek:
        #print(i)
        for j in i:
            #print(j)
            if j==0:
                c+=1
    return c

print(f"Az adatbázisban {nullaKm()} db 0 km havi futásteljesítményt tartalmazó hónap van.")