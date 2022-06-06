import math 
import numpy as np

macierzT = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,-1,-1,-1,-1],
    [1,1,-1,-1,0,0,0,0],
    [0,0,0,0,1,1,-1,-1],
    [1,-1,0,0,0,0,0,0],
    [0,0,1,-1,0,0,0,0],
    [0,0,0,0,1,-1,0,0],
    [0,0,0,0,0,0,1,-1]
]
)

macierz = macierzT.T
# macierz = macierz @ macierzT
# macierzjed = []
# for wektor in macierz:
#     dl = math.sqrt(np.dot(wektor, wektor))
#     wektor = wektor / dl
#     macierzjed.append(wektor)

# macierzjed = np.array(np.transpose(macierzjed))

wek = np.array([8,6,2,3,4,6,6,5])
wekT = wek.T
macierzT = macierzT @ wekT

print(macierzT)