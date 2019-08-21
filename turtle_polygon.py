import turtle
paper = turtle.Screen()
pen = turtle.Turtle()
pen.color("blue")
for i in range(3):
    pen.forward(50)
    pen.left(120)
pen.penup()
pen.forward(75)
pen.color("pink")
pen.pendown()
for i in range(3):
    pen.forward(50)
    pen.left(120)
pen.penup()
pen.forward(75)
pen.color("green")
pen.pendown()
for i in range(3):
    pen.forward(50)
    pen.left(120)     #3 triangles
pen.penup()
pen.bk (300)
pen.pendown()
pen.circle(50, 360, 6) #hexagon
