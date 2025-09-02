import turtle 
t = turtle.Turtle()

# svetafor korpusi
t.penup()
t.goto(-100, -160)
t.pendown()
t.color("black")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.end_fill()

# Qizil chiroq
t.penup()
t.goto(-50, 170)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

# sariq chiroq
t.penup()
t.goto(-50, 50)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# yashil chiroq
t.penup()
t.goto(-50, -70)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()