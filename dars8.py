import matplotlib.pyplot as plt
import numpy as np

# #1
# x = [0,1,2,3,4,5,6,7,8,9]
# y = [1,3,5,7,9,11,13,15,17,19]

# plt.plot(x, y)
# plt.title("y = 2x + 1")
# plt.xlabel("x qiymati")
# plt.ylabel("y qiymati")
# plt.show()

# #2
# x = np.linspace(0, 2 * np.pi, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, 'r-', label='sin(x)')
# plt.plot(x, y2, 'b--', label='cos(x)')

# plt.title("sin(x) va cos(x) funksiyalari")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.grid(True)
# plt.show()

# #3
# x = [1,2,3,4,5,6,7,8]
# y = [1,4,9,16,25,36,49,64]

# plt.plot(x, y, color='green')
# plt.title("y = x^2 Parabolik grafik")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(True)
# plt.show()

# #4
# x = np.linspace(-5, 5, 100)
# y = x ** 3

# plt.plot(x, y, 'm')
# plt.title("y = x^3 funksiyasi grafigi")
# plt.xlabel("x o‘qi")
# plt.ylabel("y o‘qi")
# plt.grid(True)
# plt.show()

#5
# x = [1, 2, 3, 4, 5]
# y = [5, 7, 4, 6, 8]

# plt.scatter(x, y, color='orange', marker='o')
# plt.title("Scatter grafiki")
# plt.xlabel("x qiymatlari")
# plt.ylabel("y qiymatlari")
# plt.grid(True)
# plt.show()

#6
# mevalar = ['olma', 'banan', 'apelsin']
# miqdor = [10, 20, 15]

# plt.bar(mevalar, miqdor, color='skyblue')
# plt.title("Mevalar miqdori")
# plt.xlabel("Mevalar")
# plt.ylabel("Miqdor")
# plt.grid(axis='y')
# plt.show()

# #7
# mahsulotlar = np.random.normal(loc=0, scale=1, size=1000)

# plt.hist(mahsulotlar, bins=30, color='purple', edgecolor='black')
# plt.title("Normal taqsimotdagi qiymatlar gistogrammasi")
# plt.xlabel("Qiymatlar")
# plt.ylabel("Tezlik")
# plt.grid(True)
# plt.show()

# #8
# yollar = ['Avtomobil', 'Velosiped', 'Piyoda']
# foiz = [60, 25, 15]

# plt.pie(foiz, labels=yollar, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
# plt.title("Transportdan foydalanish ulushi")
# plt.show()


# #9
# kategoriyalar = ['2023', '2024', '2025']
# sotuv1 = [100, 120, 140]
# sotuv2 = [90, 110, 130]

# x = np.arange(len(kategoriyalar))
# width = 0.35

# plt.bar(x - width/2, sotuv1, width, label='Mahsulot A')
# plt.bar(x + width/2, sotuv2, width, label='Mahsulot B')

# plt.xlabel("Yillar")
# plt.ylabel("Sotuvlar")
# plt.title("Mahsulotlar sotuvining taqqoslanishi")
# plt.xticks(x, kategoriyalar)
# plt.legend()
# plt.grid(axis='y')
# plt.show()


# #10
fanlar = ['Matematika', 'Fizika', 'Ingliz tili', 'Tarix']
baholar = [85, 90, 75, 80]

plt.bar(fanlar, baholar, color='teal')
plt.title("O‘quvchilarning fanlardan baholari")
plt.xlabel("Fanlar")
plt.ylabel("Baholar (%)")
plt.ylim(0, 100)
plt.grid(axis='y')
plt.show()
