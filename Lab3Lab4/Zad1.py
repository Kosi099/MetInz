import math as mth
import numpy as np
import copy
zm = open("australian.dat")
lista = []
for value in zm:
    w = list(map(lambda e: float(e),value.split()))
    lista.append(w)
def MetrykaEuklidesowa(listaA, listaB):
    e = 0
    for i in range(len(listaA)-1):
        e = e + (listaA[i]-listaB[i])**2
    wynik = mth.sqrt(e)
    return wynik
# MetrykaEuklidesowa(lista[0], lista[3])



# Praca domowa
def pracadomowa(lista):
    lista0 = []
    lista1 = []
    y = lista[0]
    for i in range(1, 5):
        w = MetrykaEuklidesowa(y, lista[i])
        if lista[i][14]==0:
            lista0.append(w)
        elif lista[i][14]==1:
            lista1.append(w)
    slownik = {
        '0': lista0,
        '1': lista1,
        }
    return slownik

print(pracadomowa(lista))


# zad2 wyznacznik macierzy kwadratowej

def wyznacznik(macierz):
    return np.linalg.det(macierz)

macierz = [[1,1,1], [3,1,0], [3,1,3]]
wyznacznik = wyznacznik(macierz)
print(wyznacznik)


def det(macierz):
    if len(macierz) == 1:
        m = macierz[0]
        return m
    elif len(macierz) == 2:
        m = macierz[0][0]*macierz[1][1] - macierz[1][0]*macierz[0][1]
        return m
    else:
        m = 0
        for i in range(len(macierz[0])):
            x = [row[:] for row in macierz][1:]
            for row in x:
                del row[i]
            m += ((-1)**i)*macierz[0][i]*det(x)    
        return m 
print(det(macierz))



x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
def zadanie1(x, lista):
    wynik = []
    for i in range(0, len(lista)):
        tmp = [0,0]
        w = MetrykaEuklidesowa(x, lista[i])
        if lista[i][14]==0:
            tmp[0] = 0
            tmp[1] = w
        elif lista[i][14]==1:
            tmp[0] = 1
            tmp[1] = w
        wynik.append(tmp)
    return wynik
print(zadanie1(x, lista))

def sortowaniedolisty(lista):
    slownik = {}
    tmp1 = []
    tmp0 = []
    for items in lista:
        if items[0] == 0:
            tmp0.append(items[1])
        elif items[0] == 1:
            tmp1.append(items[1])
    slownik = {
        0 : tmp0,
        1 : tmp1,
    }     
    return slownik 
sortowaniedolisty(zadanie1(x,lista))

def najmniejszek(slownik, k):
    tmp = []
    for key, value in slownik:
        # value.sort()
        # for i in range(k):
        #     tmp.append(value[i])
        # slownik[key] = tmp
        # tmp = []   
        print(value)
    # return slownik
print(najmniejszek(sortowaniedolisty(zadanie1(x, lista)),3))

    
    # metryka euklidesowa dla dwoch obiektow korzystajac z wektorow i operacji na wektorach