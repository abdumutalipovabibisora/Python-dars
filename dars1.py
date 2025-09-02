

# #15
# def unli(matn):
#     lis = []
#     unlilar = ["a","o","i","u","e"]
#     for harf in matn:
#         if harf.lower() in unlilar:
#             lis.append(harf)
#     print(lis)

# matn = input("matn kiriting: ")
# unli(matn)

# #                     ---royhatlar bn ishlash---

# #16
# def katta(royhat):
#     if len(royhat) == 0:
#         return "Ro'yhat bo'sh"
#     else:
#         return max(royhat)

# royhat = list(map(int, input().split()))
# print(katta(royhat))

# #17
# def kichik(royhat):
#     if len(royhat) == 0:
#         return "Ro'yhat bo'sh"
#     else:
#         return min(royhat)

# royhat = list(map(int, input().split()))
# print(kichik(royhat))

# #18
# def kvadrat(sonlar):
#     lis = []
#     if len(sonlar) == 0:
#         return "bo'sh royhat"
#     for son in sonlar:
#         lis.append(int(son)**2)
#     return lis

# sonlar = input().split()
# print(kvadrat(sonlar))
                  
# #19
# def musbat(sonlar):
#     for son in sonlar:
#         if int(son)>0:
#             print(son)

# son = input().split()
# musbat(son)

# #20
# def bir_xil(royhat,element):
#     s = 0
#     for x in royhat:
#         if x == element:
#             s+=1
#     print(s)  

# royhat = input("royhatni kiriting: ").split()            
# element = input("elementni kiriting: ")
# bir_xil(royhat,element)

# #                     ---sonlar bn ishlash---

# #21
# def tub(son):
#     if son<=1:
#         return "tub emas"
#     for i in range(2, int(son ** 0.5) + 1):
#         if son % i == 0:
#             return "tub emas"
#     return "tub son"
        
# son = int(input())
# print(tub(son))

# #22
# def fibanachi(son):
#     if son <= 0:
#         return "musbat son kiriting."
#     elif son == 1:
#         return 0
#     elif son == 2:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, son):
#             a, b = b, a + b
#         return b

# son = int(input())
# print(fibanachi(son))

# #23
# def yigindi(son):
#     s = 0
#     for i in str(son):
#         s += int(i)
#     return s

# son = int(input())
# print(yigindi(son))

# #24
# def teskari(son):
#     s = str(son)[::-1]
#     return int(s)

# son = int(input())
# print(teskari(son))

# #25
# def boluvchilar(son):
#     lis = []
#     for i in range(1, son+1):
#         if son % i == 0:
#             lis.append(i)
#     return lis

# son = int(input("son kiriting: "))
# print(boluvchilar(son))

# #                       --- qoshimcha qiziqarli masalalar---

# #26
# def birlashtirish(matn1,matn2):
#     return matn1 + " " + matn2

# matn1 = input("1-matn kiriting: ")
# matn2 = input("2-matn kiriting: ")
# print(birlashtirish(matn1,matn2))

# #27
# def takrorlanmas(royhat):
#     a = set(royhat)
#     return list(a)

# lis = input("royhat kiriting: ").split()
# print(takrorlanmas(lis))

# #28
# def UzunSoz(matn):
#     a = matn.split()
#     return max(a, key=len)

# matn = input("matn kiriting: ")
# print(UzunSoz(matn))

# #29
# def kattasi(a,b,c):
#     return max(a,b,c)

# a = int(input("son kiriting: "))
# b = int(input("son kiriting: "))
# c = int(input("son kiriting: "))
# print(kattasi(a,b,c))

#30
def ortacha(royhat):
    s = 0
    if len(royhat) == 0:
        return 0
    for son in royhat:
        s += int(son)
    hisob = s / len(royhat)
    return hisob

royhat = input("sonlar kiriting; ").split()
print(ortacha(royhat))