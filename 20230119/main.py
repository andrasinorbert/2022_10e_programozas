lista=[]

f=open("20230119/input.txt")
for i in f:
    #lista.append(int(i))
    lista.append(int(i.strip()))
f.close()

tmp=0
for i in lista:
    tmp+=i

print(lista)
print(tmp/len(lista))