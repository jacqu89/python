def readData():
    dane = []
    f = open("ex/interpolacja.txt")
    for line in f:
        w = line.split(" ")
        dane.append(line.split(" "))
    for i in range(len(dane)):
        dane[i][1] = dane[i][1].rstrip("\n")
    f.close()
    for i in range(0,len(dane)):
        for j in range(0,2):
            dane[i][j] = float(dane[i][j]) 
    return dane

def listChar(s):
    lista = []
    w = ""
    for i in range(1,2**s):             # iteracja każdego elementu od 1 do 2^n
        l = 0                           # zmienna zliczająca tylko szukane elementy
        for j in range(0,s):            # iteracja kolejnych bitów w szukanym elemencie
            if (i & 2**j) > 0:          # zlicza każdy bit gdy występuje 1
                l = l+1
        if l == s-1:                    # jeśli szukany element odpowiednią ilość bitów
            for j in range(0,s):        # ponownie iteruje po każdym bicie w celu znalezienia
                if (i & 2**j) > 0:      # i przypisania odpowiedniej litery
                    w = w+chr(j+65)     # tworzy wyraz z zebranych liter
            lista.append(w)             # i dodaje go do listy
            w = ""
    return lista

def dataList(s):
    y = readData()
    l = listChar(s)
    t = []
    w = []
    for i in range(0,len(l)):
        for j in range(0,len(l[0])):
            t.append(float(y[ord(l[i][j])-65][0]))
        w.append(t)
        t = []
    return w