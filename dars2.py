# # fayl yaratish va oqish
# #1
# with open('data.txt', 'w') as fayl:
#     fayl.write('bu yerda qandaydir matn bor\n')

# #2
# with open("data.txt", "r") as fayl:
#     matn = fayl.read()
#     print(matn)

# #3
# with open("data.txt", "a") as fayl:
#     matn = input("matn kiriting: ")
#     fayl.write("\n" + matn)

# #4
# with open("data.txt", "r") as fayl:
#     matn = fayl.read()
#     print(matn.upper())

# #5
# with open("data.txt", "r") as fayl:
#     matn = fayl.readline()
#     print(matn[::-1])

# # faylga qoshimcha malumot qoshish
# #6
# with open("data.txt", "a") as fayl:
#     fayl.write("\n" + "vaalaykum assalom")

# #7
# def sozlarni_hisoblash(fayl_nomi):
#     with open(fayl_nomi, "r") as fayl:
#         satrlar = fayl.readlines()
#     sozlar_soni = []
#     for satr in satrlar:
#         sozlar = satr.split()
#         sozlar_soni.append(len(sozlar))
#     return sozlar_soni

# sozlar_soni = sozlarni_hisoblash('python.txt')
# print(sozlar_soni)

# #9
# def umumiy_sozlar(fayl_nomi):
#     with open(fayl_nomi,"r") as fayl:
#         matn = fayl.read()
#     sozlar = matn.split()
#     return len(sozlar)

# print(umumiy_sozlar("data.txt"))

# #10
# with open("data.txt", "r") as fayl:
#     matn = fayl.read().split()
#     print(max(matn, key=len))

# # Faylga Ro‘yxat Yozish va O‘qish
# #11
# royhat = [1,2,3,"salom","maktab"]
# with open("data.txt", "w") as fayl:
#     for element in royhat:
#         fayl.write(f'{element}\n')
# with open("data.txt", "r") as fayl:
#     a = fayl.read()
#     print(a)

# #12
# import random

# with open("data.txt", "w") as fayl:
#     for _ in range(10):
#         tasodifiy = random.randint(1, 100)
#         fayl.write(f"{tasodifiy}\n")

# with open("data.txt", "r") as fayl:
#     a = fayl.read()
#     print(a)

# #13
# with open("data.txt", "r") as fayl:
#     matn = fayl.read().split()
#     for son in matn:
#         if int(son.strip()) % 2 == 0:
#             print(son)

# #14
# royhat = [1,2,3,1,2,12,3]
# with open("data.txt", "w") as fayl:
#     royhat = set(royhat)
#     royhat = list(royhat)
#     for element in royhat:
#         fayl.write(str(element) + "\n")

# #15
# royhat = [1,2,3,1,2,12,3]
# with open("data.txt", "w") as fayl:
#     for element in royhat:
#          fayl.write(str(element) + "\n")

# # Fayl Formati: JSON
# #16
# import json

# dic = {
#     "ism": "Umar",
#     "yoshi": 25,
#     "manzil": "Andijon"
# }

# with open("data.json", "w") as fayl:
#     json.dump(dic, fayl, indent=4)

# #17
# with open("data.json", "r") as fayl:
#     matn = json.load(fayl)
#     print(matn)

# #18
# yangi = {
#     "ism": "Sardor",
#     "yosh": 20,
#     "shahar": "Buxoro"
# }
# with open("data.json", "a") as fayl:
#     json.dump(yangi, fayl, indent=4)

# #19
# with open("data.json", "r") as fayl:
#     matn = json.load(fayl)
# kalit = "ism"
# if kalit in matn:
#     print(f"{kalit} : {matn[kalit]}")
# else:
#     print("malumot yoq")

# #20
# with open("data.json", "r") as fayl:
#     malumot = json.load(fayl)

# for key, value in malumot.items():
#     print(f"{key} : {value}")

# # Fayl Formati: CSV
# #21
# import csv

# malumot = [
#     ["Ism", "Yosh", "Shahar"],
#     ["Ali", 22, "Toshkent"],
#     ["Omar", 25, "Andijon"],
#     ["Umar", 24, "Buxoro"],
# ]

# with open("oquvchilar.csv", "w", newline="") as fayl:
#     yozish = csv.writer(fayl)
#     yozish.writerows(malumot)

# #22
# with open("oquvchilar.csv", "r") as fayl:
#     oqish = csv.reader(fayl)
#     for soz in oqish:
#         print(soz)

# #23
# import csv

# malumot = [
#     ["Ism", "Yosh", "Shahar"],
#     ["Ali", 22, "Toshkent"],
#     ["Omar", 25, "Andijon"],
#     ["Umar", 24, "Buxoro"],
# ]

# with open("oquvchilar.csv", "w", newline="") as fayl:
#     yozish = csv.writer(fayl)
#     yozish.writerows(malumot)

# ustun = []
# with open("oquvchilar.csv", "r") as kirish_fayl:
#     oqish = csv.reader(kirish_fayl)

#     next(oqish)
#     for qator in oqish:
#         ustun.append(qator[1])

# with open("yangi.csv", "w", newline = "") as chiqish_fayl:
#     yozish = csv.writer(chiqish_fayl)
#     for element in ustun:
#         yozish.writerow([element])

# #24
# import csv

# yangi_qator = ["vali", 30, "andijon"]

# with open("oquvchilar.csv", "a", newline = "") as fayl:
#     yozish = csv.writer(fayl)
#     yozish.writerow(yangi_qator)

#25
# import csv

# sonlar = []

# with open("yangi.csv", "r", newline = "") as fayl:
#     oqish = csv.reader(fayl)
#     next(oqish)
#     for qator in oqish:
#         for element in qator:
#             sonlar.append(element)

# katta = max(sonlar)
# kichik = min(sonlar)
# print(katta, kichik)

# Faylni O‘chirish va Nomini O‘zgartirish
# #26
# import os

# with open("keraksiz.txt", "w") as fayl:
#     fayl.write("sozlar")

# os.rename("keraksiz.txt", "python.txt")

# #27
# import os

# os.remove("python.txt")

# #28
# import os

# if os.path.getsize("python.txt") == 0:
#     os.remove("python.txt")
#     print("ochirildi")
# else:
#     print("ochirilmadi")

# #29
# import os

# if os.path.exists("python.txt"):
#     print("bor")
# else:
#     print("yoq")

# #30
# matn = "12"

# with open("data.txt", "r") as fayl:
#     oqish = fayl.read()

# if matn in oqish:
#     print(True)
# else:
#     print(False)

#8
oqish = open("python.txt", "r")
malumot = oqish.read().split()

raqamlar = open("data.txt", "a")

for element in malumot:
    if element.isdigit():
        raqamlar.write(f"{element} ")




