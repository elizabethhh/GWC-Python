import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

def drawSquare(side_length):
    for i in range(4):
        pen.forward (side_length)
        pen.right (90)
drawSquare(100)
drawSquare(50)




