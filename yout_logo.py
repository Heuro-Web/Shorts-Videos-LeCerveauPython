import turtle

# Configuration de l'écran
screen = turtle.Screen()
screen.bgcolor("white")

# Créer le stylo
t = turtle.Turtle()
t.speed(5)

# Dessin du rectangle rouge (corps du logo)
t.penup()
t.goto(-150, 90)
t.pendown()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(300)
    t.right(90)
    t.forward(180)
    t.right(90)
t.end_fill()

# Dessin du triangle blanc (play)
t.penup()
t.goto(-40, 0)
t.setheading(0)
t.color("white")
t.begin_fill()
t.pendown()
t.goto(50, 30)
t.goto(50, -30)
t.goto(-40, 0)
t.end_fill()

# Fin
t.hideturtle()
turtle.done()