# mavzu : numpy kutubxonasi 2
# 1-10. Massivlarni indekslash
import numpy as np

# # 1
# massiv = np.array([1, 2, 3, 4, 5])
# y_massiv = massiv[2]
# print(y_massiv)

# # 2
# massiv = np.array([1, 2, 3, 4, 5])
# y_massiv = massiv[-1]
# print(y_massiv)

# # 3
# massiv = np.array([[1, 2, 3],[4, 5, 6]])
# y_massiv = massiv[1, 2]
# print(y_massiv)

# # 4
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# y_massiv = massiv[2, 0]
# print(y_massiv)

# # 5
# massiv = np.array([1, 2, 3, 4, 5])
# y_massiv = massiv[::2]
# print(y_massiv)

# # 6
# massiv = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# y_massiv = massiv[[1, 3, 5]]
# print(y_massiv)

# # 7
# massiv = np.array([[1, 2, 3],[4, 5, 6]])
# y_massiv = massiv[:, 0]
# print(y_massiv)

# # 8
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# y_massiv = massiv[2]
# print(y_massiv)

# # 9
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# y_massiv = massiv[massiv > 5]
# print(y_massiv)

# 10
# massiv = np.array([[1, 2, 3, 4],[4, 5, 6, 7],[7, 8, 9, 10],[10, 11, 12, 13]])
# y_massiv = massiv[:, [1, 3]]
# print(y_massiv)

# 11-20. Massivlarni qirqib olish (slicing) 
# # 11
# massiv = np.array([1, 2, 3, 4, 5, 6 ,7 ,8, 9])
# y_massiv = massiv[:5]
# print(y_massiv)

# # 12
# massiv = np.array([1, 2, 3, 4, 5, 6 ,7 ,8, 9])
# y_massiv = massiv[-3]
# print(y_massiv)

# # 13
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# y_massiv = massiv[1:, :]
# print(y_massiv)

# # 14
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# y_massiv = massiv[:3, :]
# print(y_massiv)

# # 15
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# y_massiv = massiv[:, ::2]
# print(y_massiv)

# # 16
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# teskari = massiv[::-1, ::-1]
# print(teskari)

# # 17
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# y_massiv = massiv[:, -2:]
# print(y_massiv)

# # 18
# massiv = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
# kichik_bolak = massiv[1:4, 1:3]
# print(kichik_bolak)

# # 19
# massiv = np.array([[1, -2, 3],[-4, 5, -6],[7, -8, 9]])
# manfiy_elementlar = massiv[massiv < 0]
# print(manfiy_elementlar)

# # 20
# massiv = np.array([[[1, 2], [3, 4], [5, 6]],
#                    [[7, 8], [9, 10], [11, 12]],
#                    [[13, 14], [15, 16], [17, 18]]])
# bolak = massiv[0:2, 0:2, 1:3]
# print(bolak)

# # 21-30. Ma'lumot turlari bilan ishlash
# # 21
# massiv = np.array([[1, 2, 3],[4, 5, 6]])
# malumot_turi = massiv.dtype
# print(malumot_turi)

# # 22
# massiv = np.array([[1, 2, 3],[4, 5, 6]])    
# y_massiv = massiv.astype(float)
# print(y_massiv)

# # 23
# massiv = np.array([[1.5, 2.7, 3.3],[4.8, 5.1, 6.9]])   
# y_massiv = massiv.astype(int)
# print(y_massiv)

# # 24
# massiv = np.array([[1, 0, 3],[4, 0, 6]])
# boolean = massiv.astype(bool)
# print(boolean)

# # 25
# massiv = np.array([[1, 0, 3],[4, 0, 6]])
# string = massiv.astype(str)
# print(string)

# # 26
# massiv = np.array([[1, 2, 3],[4, 5, 6]])  
# floatt = massiv.astype(float)
# print(floatt)

# # 27
# massiv = np.array([1, 2.5, "Hello", True], dtype=object)
# for elem in massiv:
#     print(type(elem))

# # 28
# massiv = np.array([1, "hello", 3.5, [1, 2, 3]], dtype=object)
# print(massiv)

# # 29
# massiv = np.array([1, 2.5, 3, 4.0])
# print(massiv.dtype)

# 30
dtype = np.dtype([('integer', np.int32), ('float_num', np.float64)])
massiv = np.array([(1, 1.5), (2, 2.5), (3, 3.5)], dtype=dtype)
print(massiv)
