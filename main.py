

import turtle
arrow = turtle.Turtle()
def star(x, y, color, length):
    arrow.up()
    arrow.goto(x, y)
    arrow. setheading(157)
    arrow.pendown()
    arrow.begin_fill()
    arrow.color(color)
    for star in range(0, 8):
        arrow.pensize(3)
        arrow.forward(length)
        arrow.right(135)
    arrow.end_fill()

def greensqr():
    arrow.pendown()
    arrow.color('#509e2f')
    arrow.begin_fill()
    arrow.forward(500)
    arrow.right(90)
    arrow.forward(100)
    arrow.right(90)
    arrow.forward(500)
    arrow.right(90)
    arrow.end_fill()
    arrow.penup()

def bluesqr():
    arrow.pendown()
    arrow.color('#00b5e2')
    arrow.begin_fill()
    arrow.forward(300)
    arrow.right(90)
    arrow.forward(500)
    arrow.right(90)
    arrow.forward(100)
    arrow.right(90)
    arrow.forward(500)
    arrow.end_fill()
    arrow.penup()

def redsqr():
    arrow.pendown()
    arrow.color('#ef3340')
    arrow.begin_fill()
    arrow.left(90)
    arrow.forward(100)
    arrow.left(90)
    arrow.forward(500)
    arrow.left(90)
    arrow.forward(100)
    arrow.end_fill()
    arrow.penup()
def drawmoon(x, y, color, radius):
    arrow.penup()
    arrow.goto(x, y)
    arrow.color(color)
    arrow.begin_fill()
    arrow.circle(radius)
    arrow.end_fill()
def text():
    arrow.penup()
    arrow.goto(-565,150)
    arrow.color("Dark green")
    arrow.begin_fill()
    arrow.goto(-565,100)
    arrow.write(('Türkiye & Azerbaycan'), move=False, align="Left", font=("Flux Regular", 19, "normal"))
    arrow.goto(-565,50)
    arrow.write(('İki devlet bir millet'), move=False, align="Left", font=("Flux Regular", 19, "normal"))
    arrow.end_fill()
def text1():
    arrow.goto(-7,200)
    arrow.write(('Azerbaycan'), move=False, align="Left", font=("Flux Regular", 19, "normal"))
    arrow.goto(25,-270)
    arrow.write((""" hpitgroup.glitch.me"""), move=False, align="Left", font=("Flux Regular", 14, "normal"))
for i in range(1):
    greensqr()
    bluesqr()
    redsqr()
    drawmoon(280, 52, "white", 44)
    drawmoon(282, 52, '#ef3340', 36)
    star(297, 33, "white", 40)
    text()
    text1()

turtle.done()

