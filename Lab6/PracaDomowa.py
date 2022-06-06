import math 
import numpy as np

# x = [1, 3]
# y = [5, 7]

# def srednia_wektorowa(x, y):
#     wynik = 0
#     for a, b in zip(x, y):
#         print(a, b)
#         wynik += a+b

#     return wynik/(len(x))

# print(srednia_wektorowa(x, y))

def srednia(vector):
    vector_1 = np.ones(len(vector))
    return np.dot(vector, vector_1) / len(vector)


def wariancja(vector):
    sr = srednia(vector)
    vector_srednich = sr * np.ones(len(vector))
    vector_1 = vector - vector_srednich
    return np.dot(vector_1, vector_1)/len(vector)


def odchylenie_standardowe(vector):
    return math.sqrt(wariancja(vector))
vector = np.array([1,2,3])
print(vector)
print(srednia(vector))
print(wariancja(vector))
print(odchylenie_standardowe(vector))
# print(np.var(vector))