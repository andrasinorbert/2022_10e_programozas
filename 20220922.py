

t=[32,43,10,3,7,5]

# összegzés (sorozatszámitás) tétele
s=0
for i in t:
    s+=i
    
print("A lista elemeinek összege: ", s)
print("A lista elemeinek összege: ", sum(t))


# Megszámlálás tétele
db=0
for i in t:
    if i % 2==0:
        db+=1
print("Páros számok darabszáma: ", db)

# Max kiválasztása
max_index=0
max_ertek=t[0]

for i in range(0,len(t)):
    if max_ertek<t[i]:
        max_ertek=t[i]
        max_index=i
print("A max érték és indexe: ", max_ertek, max_index)

def sorozatszamitasTetele(tomb):
    s=0
    for i in tomb:
        s+=i
    return s

tomb2=[5,6,8,3,20,1]

print("Elemek összege:", sorozatszamitasTetele(tomb2) )

def ki(str):
    print(str)
    
ki("valami")
"""
def generateRandomIntNums(db, legkisebbszam=0, legnagyobbszam=100):
    import random
    tomb=[]
    for i in range(0,db):
        rnd=random.randint(legkisebbszam, legnagyobbszam)
        tomb.append(rnd)
    return tomb
        
randoms=generateRandomIntNums(db=5,legkisebbszam=2,legnagyobbszam=100)
print(randoms)


randoms=generateRandomIntNums(50)
print(randoms)
"""

import hasznosfuggvenyek

randoms=hasznosfuggvenyek.generateRandomIntNums(50)
print(randoms)
