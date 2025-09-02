# mavzu: Numpy kutubxonasi
# 1-10: Massiv yaratish bilan bog‘liq masalalar

import numpy as np 

# # 1
# a = np.array([1,2,3])
# print(a)

# # 2
# b = np.array([[1,2,3],[4,5,6]])
# print(b)

# # 3
# nollar = np.zeros((3,3))
# print(nollar)

# # 4
# birlar = np.ones((4,4))
# print(birlar)3

# # 5
# tasodif = np.random.rand(5)
# print(tasodif)

# # 6
# son = np.random.randint(10, 50, size = 10)
# print(son)

# # 7
# a = np.arange(1,21)
# b= a.reshape(2, 10)
# print(b)

# # 8
# d = np.diag([1,2,3,4,5,6,7])
# print(d)

# c = np.eye(7, 7)
# print(c)

# # 9
# son = np.arange(1, 101)
# teskari = son[::-1]
# print(teskari)

# # 10
# matritsa = np.random.randint(1, 10, size = (3, 3))
# ortacha = np.mean(matritsa)
# print(ortacha)

# # 11-20: Massivga element qo‘shish bilan bog‘liq masalalar
# # 11
# massiv = np.random.rand(5)
# yangi = 10
# massiv = np.append(massiv, yangi)
# print(massiv)

# # 12  
# massiv = np.random.randint(1, 100, size = 10)
# yangi = 100
# massiv = np.insert(massiv, 2, yangi)
# print(massiv)

# # 13
# matritsa = np.random.randint(1, 10, size = (4, 4))
# qator = np.array([1, 2, 3, 4])
# matritsa = np.vstack([matritsa, qator])
# print(matritsa)

# # 14
# m = np.random.randint(1, 10, size = (3, 3))
# ustun = np.array([1, 2, 3])
# m = np.hstack((m, ustun.reshape(-1, 1)))
# print(m)
                        
# # 15
# massiv = np.random.randint(1, 10, size = (2, 5))
# yangi = np.array([6, 6])
# massiv = np.hstack((massiv, yangi.reshape(-1, 1)))
# print(massiv)

# 16
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# yangi = [11,12,13]
# a = np.append(a, yangi)
# print(a)

# # 17
# m = np.array([1,2,3])
# m = np.tile(m, 2)
# print(m)

# # 18
# matritsa = np.random.randint(1, 10, size = (4, 4))
# yangi = np.array([5,5,5,5])
# matritsa = np.vstack([matritsa, yangi])
# print(matritsa)

# # 19
# matritsa = np.random.randint(1, 10, size = (3, 3))
# matritsa = matritsa + 2
# print(matritsa)

# # 20
# matritsa = np.random.randint(1, 10, size = 10)
    # yangi = 20
# matritsa = np.append(matritsa, yangi)
# matritsa = np.sort(matritsa)
# print(matritsa)

# # 21-30: Massivdan element o‘chirish bilan bog‘liq masalalar
# # 21
# massiv = np.arange(10)
# massiv = np.delete(massiv, 4)
# print(massiv)

# # 22
# matritsa = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# matritsa = np.delete(matritsa, 1, axis = 0)
# print(matritsa)

# # 23
# matritsa = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# matritsa = np.delete(matritsa, 0, axis = 1)
# print(matritsa)

# # 24
# matritsa = np.arange(1, 11)
# matritsa = np.delete(matritsa, [2, 6])
# print(matritsa)

# # 25
# massiv = np.array([2, 6, 1, 12, 45, 0])
# katta = np.max(massiv)
# kichik = np.min(massiv)
# massiv = np.delete(massiv, np.where(massiv == katta))
# massiv = np.delete(massiv, np.where(massiv == kichik))
# print(massiv)

# # 26
# matritsa = np.random.randint(1, 101, size=(6, 6))
# print(matritsa)
# matritsa = np.delete(matritsa, 2, axis=0)
# matritsa = np.delete(matritsa, 3, axis=1)
# print(matritsa)

# # 27
# massiv = np.random.randint(1, 101, size=10)
# print(massiv)
# yangi_massiv = []
# # for son in massiv:
#     if son % 2 != 0:
#         yangi_massiv.append(son)
# print(yangi_massiv)

# # 28
# massiv = np.random.randint(1, 101, size=7)
# print(massiv)
# massiv = np.delete(massiv, 2)
# print(massiv)

# 29
# massiv = np.random.randint(0, 11, size=8)
# print(massiv)
# yangi_massiv = []
# for son in massiv:
#     if son != 0:
#         yangi_massiv.append(son)
# print(yangi_massiv)

# 30
import random

massiv = []
for _ in range(10):
    son = random.randint(1, 20)
    massiv.append(son)
print(massiv)
yangi_massiv = list(set(massiv))
print(yangi_massiv)                                           