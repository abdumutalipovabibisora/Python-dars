# 4-masala: 5, 6, 7 va 8 uchi bo‘lgan, har bir uchi 80 piksel uzunlikdagi yulduzlarni bir qatorda chizing. 

import turtle

turtle.penup()
x_pos = -300

sizes = [5, 6, 7, 8]

for size in sizes:
    turtle.goto(x_pos, 0)
    turtle.pendown()

    for _ in range(5):
        turtle.forward(size * 20)
        turtle.right(144)

    turtle.penup()
    x_pos += 140

turtle.done()



# import turtle
# import math

# # Ekranni sozlash
# ekran = turtle.Screen()
# ekran.bgcolor("white")

# # Chizuvchi obyekt
# chiziq = turtle.Turtle()
# chiziq.speed(0)
# chiziq.color("black", "yellow")  # Qora kontur, sariq to‘ldirish

# # Doira chizish funksiyasi
# def chiz_doira(x, y, radius):
#     chiziq.penup()
#     chiziq.goto(x, y - radius)  # Doira markazidan pastga siljib boshlash
#     chiziq.pendown()
#     chiziq.begin_fill()
#     chiziq.circle(radius)
#     chiziq.end_fill()

# # Markaziy doira
# chiz_doira(0, 0, 30)

# # Tashqi 8 ta doira
# for i in range(8):
#     burchak = math.radians(i * 45)  # 360/8 = 45 gradus
#     x = 100 * math.cos(burchak)  # 100 bu tashqi doiraning markazi uchun masofa
#     y = 100 * math.sin(burchak)
#     chiz_doira(x, y, 40)

# turtle.done()