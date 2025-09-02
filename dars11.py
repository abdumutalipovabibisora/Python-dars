import matplotlib.pyplot as pl

# x = [1, 2, 3, 4, 5]
# # k = 2
# # b = 1
# y = [3, 5, 7, 9, 11]
# pl.plot(x, y, marker = "o")
# pl.xlabel("ox oqi")
# pl.ylabel("oy oqi")
# # pl.grid(True)
# pl.show() 


x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

pl.plot(x, y)
pl.xlabel('X o‘qi', fontsize=20)  # X o‘qi nomi — 14 o‘lchamli shrift bilan
pl.ylabel('Y o‘qi', fontsize=20)  # Y o‘qi nomi — 14 o‘lchamli shrift bilan

pl.title('Oddiy chizma', fontsize=16)  # Grafik sarlavhasi — 16 o‘lchamli shrift bilan

pl.show()


