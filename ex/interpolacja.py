import re
from funkcje import readData,dataList

s = 5
x = 2

data = readData()
print("wprowadzone dane:")
for i in data:
    print(i)


lista = dataList(s)
print("\nlista x0, x1, .. xn:")
for l in lista:
    print(l)


