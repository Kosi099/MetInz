import math as mth
import numpy as np

zm = open("australian.dat")
lista = []
for value in zm:
    w = list(map(lambda e: float(e),value.split()))
    lista.append(w)

def MetrykaWektory(x, y):
    wynik = 0
    for a, b in zip(x, y):
        wynik += (a - b)**2
    return mth.sqrt(wynik)

def  MetrykaWektory2(x, y, czy = False):
    if(czy == False):
        v1 = np.array(x)
        v2 = np.array(y)
    else:
        v1 = np.array(x[:-1])
        v2 = np.array(y[:-1])
    wynik = np.dot(v2-v1, v2-v1)
    wynik = np.sqrt(wynik)
    return wynik

# def srodekmasy(lista):


# program całkujący monte
