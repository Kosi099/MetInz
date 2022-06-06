# # Zad1
# zm1={
#     'Czechy': 'Praga',
#     'Słowacja': "Bratysława",
#     'Ukraina': 'Kijów',
#     'Niemcy': 'Bralin',
#     'Rosja': 'Moskwa',
#     'Białoruś': 'Mińsk',
#     'Litwa': 'Wilno',
# }
# zm1['Hiszpania']='Madryt'
# print(zm1)
# # Zad2
# print(bool(''))
# print(bool(' '))
# print(bool(0))
# print(bool(1))
# print(bool('0'))
# print(bool('1'))
# print(bool([]))
# print(bool([","]))
# # zad3
# zm = 'Metody inżynierii wiedzy'
# if('i'in zm):
#     print("Jest")
#     print(zm.count('i'))
# else:
#     print("Nie ma")
# # Zad4
# for i in range(21):
#     print(i)
# # Zad5
# zm='Ala ma kota a kot ma ale'
# x=[]
# y=''
# for i in range(len(zm)):
#     if(zm[i]!=' '):
#         y=y+zm[i]
#     else:
#         x.append(y)
#         y=''
# x.append(y)
# print(x)
# # Zad6
# haslo='TwojaStaraZapierdala!'
# def spr(x):
#     M=0
#     m=0
#     z=0
#     for i in x:
#         if(i.islower()):
#             M=M+1
#         elif(i.isupper()):
#             m=m+1
#         elif(i=='!'):
#             z=z+1
#     if(len(x)<10):
#         return False
#     elif(M==0 or m==0):
#         return False
#     elif(z==0):
#         return False
#     return True
# print(spr(haslo))
# Zad7