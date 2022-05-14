from funkcje import readData,dataList

data = readData()

s = len(data)

lista = dataList(s)

print("-"*50)
print("Wprowadzone dane:")
for i in data:
    print(i)
print("-"*50)
#print(lista)
#print("-"*50)



def wynik(x):
    b=[]
    for i in range(0,s):
        a=1
        k=1
        for j in range(0,s-1):
            a = a*(x-lista[i][j])
            k = k*(data[s-1-i][0]-lista[i][j])
        if k == 0:
            b.append(0)
        else:
            b.append(data[s-1-i][1]*(a/k))
    w=0
    for u in range(0,len(b)):
        w = w+b[u]
    return w

for i in range(-10,11):
    print("W(",i,") = ",round(wynik(i),5),sep="")