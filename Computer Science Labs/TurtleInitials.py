import turtle
#this program writes my initials using turtle graphics
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor("silver")

curtle = turtle.Turtle()
durtle = turtle.Turtle()
nurtle = turtle.Turtle()

curtle.penup()
durtle.penup()
nurtle.penup()

curtle.goto(-400, 0)
durtle.goto(-150, 200)
nurtle.goto(100, -200)

curtle.pendown()
durtle.pendown()
nurtle.pendown()

curtle.fillcolor('red')
durtle.fillcolor('black')
nurtle.fillcolor('green')

curtle.begin_fill()
durtle.begin_fill()
nurtle.begin_fill()
#below are all of the C turtles movement commands except goto
curtle.left(45)
curtle.forward(282.84)
curtle.right(135)
curtle.forward(50)
curtle.right(45)
curtle.forward(212.14)
curtle.left(90)
curtle.forward(212.14)
curtle.right(45)
curtle.forward(50)
curtle.right(135)
curtle.forward(282.84)
curtle.end_fill()
curtle.hideturtle()
#below are all of the D turtles movement commands except goto
durtle.right(45)
durtle.forward(282.84)
durtle.right(90)
durtle.forward(282.84)
durtle.right(135)
durtle.forward(400)
durtle.up()
durtle.goto(-12.5, 0)
durtle.down()
durtle.left(45)
durtle.forward(141.42)
durtle.left(135)
durtle.forward(200)
durtle.left(135)
durtle.forward(141.42)
durtle.end_fill()
durtle.hideturtle()
#below are all of the N turtles movement commands except goto
nurtle.forward(37.5)
nurtle.left(90)
nurtle.forward(300)
nurtle.right(150)
nurtle.forward(345.41)
nurtle.left(60)
nurtle.forward(37.5)
nurtle.left(90)
nurtle.forward(400)
nurtle.left(90)
nurtle.forward(37.5)
nurtle.left(90)
nurtle.forward(300)
nurtle.right(150)
nurtle.forward(345.41)
nurtle.left(60)
nurtle.forward(37.5)
nurtle.left(90)
nurtle.forward(400)
nurtle.end_fill()
nurtle.hideturtle()

screen.exitonclick()