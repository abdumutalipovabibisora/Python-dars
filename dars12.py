import turtle

t = turtle.Turtle()

n = int(input("n burchakni kiriting(n>2): "))

burchak = 360/n

for _ in range(n):
    t.forward(100)
    t.left(burchak)

turtle.done()
