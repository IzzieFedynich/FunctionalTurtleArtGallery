import turtle
turtle.shape("turtle")
turtle.speed(1000)

def star(sidelength):
    for i in range(5):
        turtle.forward(sidelength)
        turtle.right(145)

def MiniStars():
    for i in range(4):
        turtle.penup()
        turtle.right(90)
        turtle.forward(75)
        turtle.pendown()
        star(50)

def octogon(sidelength):
    for i in range(8):
        turtle.forward(sidelength)
        turtle.right(45)

def OctogonSpiral():
    for i in range(35):
        octogon(i*2)
        turtle.right(5)

def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)

def SquareCircle():
    for i in range(77):
        square(1*20)
        turtle.right(5)

def SquareSpiral():
    for i in range(40):
        square(i*5)
        turtle.right(5)

def triangle(sidelength):
    for i in range(3):
        turtle.forward(sidelength)
        turtle.right(130)

def TriangleSpiral():
    for i in range(25):
        triangle(i*5)
        turtle.right(5)

turtle.bgcolor("light cyan")

MiniStars()
turtle.penup()
turtle.goto(345,345)
turtle.pendown()
turtle.color("rosy brown")
OctogonSpiral()
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()
turtle.color("sandy brown")
SquareCircle()
turtle.penup()
turtle.goto(300,-300)
turtle.pendown()
turtle.color("gold")
TriangleSpiral()
turtle.color("orange")
turtle.penup()
turtle.goto(-320,300)
turtle.pendown()
TriangleSpiral()
turtle.penup()
turtle.goto(-400,0)
turtle.color("light coral")
turtle.pendown()
SquareSpiral()
turtle.penup()
turtle.goto(400,0)
turtle.pendown()
turtle.color("light coral")
SquareSpiral()
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.color("Salmon")
SquareCircle()



turtle.exitonclick()
