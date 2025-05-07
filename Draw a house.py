import turtle

t = turtle.Turtle()
t.speed(1)
t.width(3)

# --- Corps de la maison ---
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("#F4A460")  # beige
t.begin_fill()
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

# --- Toit ---
t.penup()
t.goto(-120, 50)
t.pendown()
t.color("#8B0000")
t.begin_fill()
t.goto(0, 150)
t.goto(120, 50)
t.goto(-120, 50)
t.end_fill()

# --- Porte ---
t.penup()
t.goto(-30, -100)
t.pendown()
t.color("saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(120)
    t.left(90)
t.end_fill()

# Poignée de porte
t.penup()
t.goto(20, -40)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(5)
t.end_fill()

# --- Fenêtres avec cadre, croisillons, et reflet ---
def draw_window(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

    # Cadre (épais)
    t.color("black")
    for _ in range(4):
        t.forward(50)
        t.left(90)

    # Croisillons
    t.penup()
    t.goto(x + 25, y)
    t.setheading(90)
    t.pendown()
    t.forward(50)

    t.penup()
    t.goto(x, y + 25)
    t.setheading(0)
    t.pendown()
    t.forward(50)

    # Reflet (diagonale bleue claire)
    t.penup()
    t.goto(x + 5)
    t.pendown()
    t.color("#cceeff")
    t.setheading(-45)
    t.width(1)
    t.forward(20)

# Fenêtres gauche et droite
draw_window(-80, -10)
draw_window(30, 0)

t.hideturtle()
turtle.done()