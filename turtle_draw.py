import turtle
pen= turtle.Turtle()
paper= turtle.Screen()
def drawPolygonFlower (color, length, numberOfSides): #color input must be a string
    for i in range(8):
        pen.color(color)
        pen.circle(length,360,numberOfSides)
        pen.left(45)

drawPolygonFlower("purple", 25, 50)
drawPolygonFlower("pink", 50, 9)
drawPolygonFlower("blue", 60, 5)

pen.penup()
pen.goto(-150,0)

def drawHeart (color, size_length): #color input as a string
    pen.pendown()
    pen.color(color)

    pen.left(45)
    pen.fd(size_length)
    pen.circle(size_length/2,180)

    pen.right(90)
    pen.circle(size_length/2,180)
    pen.fd(size_length)

drawHeart("red", 50)


    




       


