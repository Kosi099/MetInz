import math
import numpy as np

def fun(macierz):
    # v=>u=>e
    listau = []
    listae = []
    print("A = ", macierz)
    # Liczenie u
    for i in range(len(macierz)):
        if i == 0:
            u = macierz[i]
            listau.append(u)
        else:
            projekcja = listau[i-1].copy()
            for l in range(len(listau[i-1])):
                projekcja[l] = projekcja[l]*(np.dot(macierz[i], listau[i-1]) / np.dot(listau[i-1],listau[i-1]))
            un = macierz[i]
            for k in range(len(un)):
                un[k] = un[k]-projekcja[k]
            listau.append(un)
    print("u = ",listau)
    # Liczenie e
    for j in range(len(macierz)):
        bu = 0
        for x in range(len(listau[j])):
            bu = bu + (listau[j][x]**2)
        bu = np.sqrt(bu)
        e = listau[j].copy()
        for y in range(len(listau[j])):
            e[y]=e[y]/bu
        listae.append(e)
    print("Q = ", listae)

A = [
    [2,1,0],
    [0,1,2],
]
fun(A)