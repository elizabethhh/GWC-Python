import turtle
pen = turtle.Turtle()
paper = turtle.Screen()

def drawHeart (color, size_length): #color input as a string
    pen.color(color)

    pen.left(45)
    pen.fd(size_length)
    pen.circle(size_length/2,180)

    pen.right(90)
    pen.circle(size_length/2,180)
    pen.fd(size_length)

drawHeart("purple", 50)


