import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

def drawTriangle(side_length):
    for i in range(3):
        pen.forward (side_length)
        pen.left (120)
drawTriangle(100)
drawTriangle(50)




