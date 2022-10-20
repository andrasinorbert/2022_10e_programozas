X=[10,8,87,60,12]
MaxÉrt=X[0]
MaxIndex=0
for i in range(1, len(X)-1):
    if( MaxÉrt< X[i]):
        MaxÉrt=X[i]
        MaxIndex=i
print("Max: X[",MaxIndex,"]=",MaxÉrt)

print(max(X))

# Harmonikus közép
def HarmonikusKozep(list):
    s=0
    for i in range(len(list)):
        s+= 1/list[i]
    return len(list)/s


X=[2,4,16]
print("HarmKözép:",HarmonikusKozep(X))
print("HarmKözép:",HarmonikusKozep([4,6,32,12,6]))

list=[2,3,4,5]
a=list
a[1]=10
print(list) #2,3,4,5
b=list[:]
b[2]=15
print(list) #2,3,4,5

def listazas(lista):
    lista[1]=0
    
l=[1,1,1,1,1,1,1]
listazas(l[:])
print(l)