from operator import le
import re
from funkcje import readData,dataList

s = 5
x = 2

data = readData()
lista = dataList(s)

print("-"*50)
print("Wprowadzone dane:")
for i in data:
    print(i)
print("-"*50)



def wynik(x):
    b=[]
    for i in range(0,s-1):
        a=1
        k=1
        for j in range(0,s-1):
            a = a*(x-lista[0][j])
            k = k*(data[s-1][1]-lista[0][j])
        b.append(data[s-1-i][1]*(a/k))
    #print(b)                       #wynik dla każdego nawiasu
    w=0
    for u in range(0,len(b)):
        w = w+b[u]
    return w

g = wynik(x)
print(g)