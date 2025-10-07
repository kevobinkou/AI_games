import turtle
import math
import colorsys
import time

# --- Setup the screen ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Wave Motion - KELVIN MAINA says WANTAM")
screen.tracer(0)

# --- Turtle setup ---
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

message = "KELVIN MAINA says WANTAM"
font_size = 28
amplitude = 50   # height of the wave
wavelength = 25  # horizontal spacing
speed = 0.15     # wave movement speed

# --- Main animation loop ---
for frame in range(200):
    t.clear()
    for i, ch in enumerate(message):
        # Color smoothly cycles through the rainbow
        hue = ((i / len(message)) + frame / 50) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        screen.colormode(1.0)
        t.color(r, g, b)

        # Calculate wave position
        x = -len(message) * 10 + i * wavelength
        y = math.sin((i + frame * speed)) * amplitude

        t.penup()
        t.goto(x, y)
        t.write(ch, align="center", font=("Courier", font_size, "bold"))
    
    screen.update()
    time.sleep(0.05)

# --- Final steady text ---
t.clear()
t.goto(0, 0)
t.color("white")
t.write("KELVIN MAINA says WANTAM", align="center", font=("Arial", 36, "bold"))
screen.update()
time.sleep(2)
turtle.done()
