import math


def metryka_euklidesowa_wektory(x, y):
    wynik = 0
    for a, b in zip(x, y):
        wynik += (a - b)**2
    return math.sqrt(wynik)


print(metryka_euklidesowa_wektory([1,2, 3], [3,4, 6]))