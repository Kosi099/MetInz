# [v1......v2]
# baza ortonormalna vectoru AtA
# Avi baza ortogonalna
# dwa wektory są ortagonalne gdy ich iloczyn skalarny wynosi 0
# (Avi)T (Avi) = viTATAvi
# Av = lambdav
# ATAv = lambdav
# (Avi)T (Avi) = viTATAvi = viT lambdai vi = lambdai viTvi = lambdai * 0 = 0


# dł(Avi) = sqrt((Avi)T(Avi)) iloczyn skalarny = sqrt(lambdai) = sigmai
# (Avi)T (Avi) = viT AT Avi = viT lambdai vi = lambdai viT vi = lambdai
# sigmai = sqrt(lambdai)
# ui = Avi/sigmai
# ui * sigmai = Avi
# Avi = ui sigmai
# Av = u sigma
# AvvT = u sigma vT
# A = u sigma vT
# vvT macierz jednostkowa = 1
# A = u sigma vT


# A = 
# [1 2 0]
# [2 0 2]

# AAT = 
# [1 2 0]     [1 2]
# [2 0 2]     [2 0]   =   [5 2]           [5-lambda 2]        (5-lambda)(8-lambda) - 2 = lambda^2 - 13lambda + 36 = 0
# ``          [0 2]       [2 8]           [2 8-lambda]            lambda1 = 9     lambda2 = 4


# [5-9 2] [u1^1]  = 0
# [2 8-9] [u1^2]

# -4u1^1 + 2u1^2 = 0
#  2u1^1 + u1^2 = 0
# 2u1^1 = u1^2

# u1 = alfa[1 2]T
# u1 = 1/sqrt(5) [1 2]T    sqrt(1^2 * 2^2) = sqrt(5)
# u2 = 1/sqrt(5)[2 -1]T

# ATA = [1 2]  [1 2 0] = [5 2 4]
#       [2 0]  [2 0 2]   [2 4 0]
#       [0 2]            [4 0 4]


# v1 = 1/3 sqrt(5) * [5 2 4]
#v2 = 1/3 sqrt(5) *  [0 2 -1]
#v3 = 1/3 sqrt(5) * [-2 1 2]


# A = 
# [1 2 0]
# [2 0 2]