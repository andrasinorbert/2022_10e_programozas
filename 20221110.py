# Adott egy számokat tartalmazó A lista és egy B szám.
# Adjunk meg két olyan elemet az A-ból, amelyek szorzata éppen a B!

A=[2,3,4,5,6,7,8,9]
B=15


def T(e):
    j=0
    global masikszam
    while j<len(A) and e*A[j] != B :
        j+=1
    van=j<len(A)
    masikszam=A[j] if van else 0
    return van

i=0
while i<len(A) and not(T(A[i])):
    i+=1
Van=i<len(A)
# másik szám egyszerűen: int(B/A[i])
print(f"A két szám: {A[i]} és { masikszam}" if Van else f"Nincs ilyen szám")

