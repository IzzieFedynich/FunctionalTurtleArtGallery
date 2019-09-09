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
MiniStars()
turtle.penup()
turtle.goto(345,345)
turtle.pendown()
def octogon(sidelength):
    for i in range(8):
        turtle.forward(sidelength)
        turtle.right(45)

def OctogonSpiral():
    for i in range(35):
        octogon(i*2)
        turtle.right(5)

OctogonSpiral()
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)

def SquareSpiral():
    for i in range(77):
        square(1*20)
        turtle.right(5)
SquareSpiral()
def triangle(sidelength):
    for i in range(3):
        turtle.forward(sidelength)
        turtle.right(130)
turtle.penup()
turtle.goto(300,-300)
turtle.pendown()


turtle.exitonclick()