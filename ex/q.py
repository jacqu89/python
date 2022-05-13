s = 5                           # stopień wielomianu
g = [[-10.0, -5.0, 0.0, 5.0, 10.0],
     [201.0, -386.5, 1.0, -361.5, -199.0]]

def readData():                 # odczyt z pliku
    q = []
    data = open("ex/dane.txt", "r")
    for line in data:
        q.append(line)
    data.close()

    for i in range(len(q)):
        w = q[i]
        q[i] = w.split(" ")
        q[i][1] = q[i][1].rstrip("\n")
    print(q)
    return q

def supplemenTable(s):              # x - po ile elementow, np, dla 2 AB...
    t = []
    v = 0
    for i in range(1, 2**s):        # iteracja po wszystkich liczbach od 1 do s potęgi dwojki 
        b = 0
        for j in range(0, s):       # iteracja po konkretnych bitach
            if (i & 2**j) > 0:      # sprawdza która iteracja 'i' posiada np cztery->1 z pięciu elementów
                b = b+1             # b zlicza występowanie 1
        if b == s-1:                # jeśli jest o jeden mniej niż szukany wielomian
            t.append("")            # dodaje do listy
            for j in range(0,s):    # i ponownie sprawdzam gdzie występują 1 i zapisuje poszczególnie znaki do listy
                if (i & 2**j) > 0:
                    t[v] = t[v]+chr(65+j)
            v = v+1                 # v jest wykorzystane do dodawania kolejnego elementu do listy 

    print("-"*50)
    print("Ilosc kombinacji: ", len(t))
    print(t)
    print("-"*50)
    return t

def interpolacja():

    print()

def wynik(s):
    a = supplemenTable(s)
    s = readData()

wynik(s)

# for i in range(len(r)):
#     for j in range(0,len(r[0])):
#         print(g[1][ord(r[i][j])-65])
#     print()