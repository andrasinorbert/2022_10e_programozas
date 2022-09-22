
def generateRandomIntNums(db, legkisebbszam=0, legnagyobbszam=100):
    import random
    tomb=[]
    for i in range(0,db):
        rnd=random.randint(legkisebbszam, legnagyobbszam)
        tomb.append(rnd)
    return tomb