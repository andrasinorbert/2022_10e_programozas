import fvek

l=[2,3,4]
fvek.szamtani(l)

lista=[]
f=open("20230126/input.txt")
for i in f:
    #lista.append(int(i))
    #lista.append(int(i.split(" ")))
    
    a=i.split(" ")
    for i in a:
        x=int(i.strip())
        lista.append(x)
f.close()

print(lista)