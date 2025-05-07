import turtle

# Configuration initiale
t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("black")
t.width(30)

# Partie rouge du logo
t.penup()
t.goto(0, 0)
t.pendown()
t.color("#db0f3c")
t.left(180)
t.circle(50, 270)
t.forward(120)
t.left(180)
t.circle(50, 90)

# Partie bleu ciel du logo
t.penup()
t.goto(-5, 13)
t.pendown()
t.color("#50ebe7")
t.left(180)
t.circle(50, 270)
t.forward(120)
t.left(180)
t.circle(50, 90)

# Partie blanche du logo
t.penup()
t.goto(-5, 5)
t.pendown()
t.color("white")
t.left(180)
t.circle(50, 270)
t.forward(120)
t.left(180)
t.circle(50, 90)

t.hideturtle()
turtle.done()