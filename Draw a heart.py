import turtle
import time

# Initialisation
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.color("red", "pink")
t.width(3)
t.speed(0)

def draw_heart(scale=1):
    t.penup()
    t.goto(0, -100 * scale)
    t.setheading(0)
    t.pendown()

    t.begin_fill()
    t.left(140)
    t.forward(180 * scale)
    t.circle(-90 * scale, 200)
    t.left(120)
    t.circle(-90 * scale, 200)
    t.forward(180 * scale)
    t.end_fill()
    t.setheading(0)

# Pulsation (agrandissement et rétrécissement)
for i in range(3):
    t.clear()
    draw_heart(1.0)
    time.sleep(0.2)
    t.clear()
    draw_heart(1.1)
    time.sleep(0.2)
    t.clear()
    draw_heart(1.0)
    time.sleep(0.2)

# Message final
t.penup()
t.goto(0, -200)
t.color("black")
t.write("Love in Python!", align="center", font=("Arial", 16, "bold"))

t.penup()
t.goto(0, -300)
t.color("black")
t.write("Backend Developer", align="center", font=("Arial", 20, "bold"))


t.hideturtle()
turtle.done()