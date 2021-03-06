import turtle

screen = turtle.Screen()
screen.bgcolor("silver")
screen.setup(1.0, 1.0)
def drawC(x, y, color):
    gt = turtle.Turtle()
    gt.fillcolor(color)
    gt.begin_fill()
    gt.penup()
    gt.goto(x, y)
    gt.pendown()
    gt.forward(300)
    gt.right(90)
    gt.forward(50)
    gt.right(90)
    gt.forward(250)
    gt.left(90)
    gt.forward(200)
    gt.left(90)
    gt.forward(250)
    gt.right(90)
    gt.forward(50)
    gt.right(90)
    gt.forward(300)
    gt.right(90)
    gt.forward(300)
    gt.end_fill()
def drawO(x, y, color):
    ot = turtle.Turtle()
    ot.fillcolor(color)
    ot.penup()
    ot.goto(x, y) 
    ot.begin_fill()
    ot.pendown()
    '''commented out because there is no fun allowed in this class, >:(
    ot.pendown()
    ot.circle(150)
    ot.left(90)
    ot.penup()
    #ot.forward(300)
    ot.forward(50)
    ot.pendown()
    ot.right(90)
    ot.circle(100)'''
    for o in range(4):
        ot.forward(300)
        ot.right(90)
    ot.end_fill()
    ot.penup()
    ot.goto(x+50, y-50)
    ot.fillcolor("silver")
    ot.begin_fill()
    ot.pendown()
    for o in range(4):
        ot.forward(200)
        ot.right(90)
    ot.end_fill()
def drawG(x, y, color):
    ct = turtle.Turtle()
    ct.penup()
    ct.fillcolor(color)
    ct.goto(x, y)
    ct.begin_fill()
    ct.pendown()
    ct.forward(300)
    ct.right(90)
    ct.forward(50)
    ct.right(90)
    ct.forward(250)
    ct.right(270)
    ct.forward(200)
    ct.right(270)
    ct.forward(200)
    ct.right(270)
    ct.forward(50)
    ct.right(270)
    ct.forward(100)
    ct.right(90)
    ct.forward(50)
    ct.right(90)
    ct.forward(150)
    ct.right(90)
    ct.forward(150)
    ct.right(90)
    ct.forward(300)
    ct.right(90)
    ct.forward(300)
    ct.end_fill()
def drawSC(x, y, color, offset):
    drawC(x-offset, y-offset, "black")
    drawC(x, y, color)
def drawSO(x, y, color, offset):
    drawO(x-offset, y-offset, "black")
    drawO(x, y, color)
def drawSG(x, y, color, offset):
    drawG(x-offset, y-offset, "black")
    drawG(x, y, color)
drawC(-550, 400, "royalblue")
drawO(-150, 400, "darkred")
drawG(250, 400, "springgreen")
drawSC(-550, 0, "royalblue", 25 )
drawSO(-150, 0, "darkred", 25)
drawSG(250, 0, "springgreen", 25)

screen.exitonclick()
