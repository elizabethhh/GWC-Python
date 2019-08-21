import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
def triangle(side_length, fill_color):
    pen.fillcolor(fill_color)
    pen.pendown()
    for i in range(3):
        pen.forward(side_length)
        pen.right(120)
        print("I just turned right!")

triangle(50, "purple")
