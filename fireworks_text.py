import turtle
import random
import colorsys
import time

# --- Setup the screen ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Fireworks Text - KELVIN MAINA says WANTAM")
screen.tracer(0)

# --- Create turtle for text and fireworks ---
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)

# --- Draw text in center ---
pen.color("white")
pen.penup()
pen.goto(0, 0)
pen.write("KELVIN MAINA says WANTAM", align="center", font=("Arial", 30, "bold"))
pen.pendown()

# --- Create fireworks turtle ---
fw = turtle.Turtle()
fw.hideturtle()
fw.speed(0)
fw.width(2)

def draw_firework(x, y):
    hue = random.random()
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    screen.colormode(1.0)
    fw.pencolor(r, g, b)

    fw.penup()
    fw.goto(x, y)
    fw.pendown()

    # Firework burst
    for i in range(20):
        fw.forward(random.randint(30, 100))
        fw.backward(random.randint(30, 100))
        fw.right(360 / 20)

    # Fading effect
    fw.penup()
    fw.goto(x, y)
    fw.pendown()
    fw.pencolor(0, 0, 0)
    fw.circle(3)

# --- Launch multiple fireworks ---
for i in range(15):
    x = random.randint(-300, 300)
    y = random.randint(-150, 250)
    draw_firework(x, y)
    screen.update()
    time.sleep(0.3)

# --- End message ---
pen.penup()
pen.goto(0, -200)
pen.color("gold")
pen.write("🎆 Celebration Complete! 🎆", align="center", font=("Courier", 18, "italic"))

screen.update()
time.sleep(2)
turtle.done()
