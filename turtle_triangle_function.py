import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

def drawPolygon(number_of_sides, side_length, color):
    pen.color(color) #color must be input as string
    for i in range(number_of_sides):
        pen.forward (side_length)
        pen.left (360/number_of_sides)
drawPolygon(6, 50, "blue")
drawPolygon(7,100,"pink")
drawPolygon(50,5,"pink") #forms a circle
drawPolygon(5,20,"maroon")




