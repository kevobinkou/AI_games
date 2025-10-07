import turtle
import time
import colorsys

# --- Setup the screen ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Neon Glow - KELVIN MAINA says WANTAM")

# --- Create the turtle ---
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(5)

# --- Rainbow text animation ---
text1 = "KELVIN MAINA"
text2 = "says WANTAM"

# Function to draw glowing text
def glowing_text(message, y, cycles=60, size=36):
    for i in range(cycles):
        hue = (i / cycles)
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        screen.colormode(1.0)
        pen.color(r, g, b)

        pen.clear()
        pen.penup()
        pen.goto(0, y)
        pen.write(message, align="center", font=("Arial", size, "bold"))
        screen.update()
        time.sleep(0.05)

# --- Animate ---
screen.tracer(0)
glowing_text(text1, 50)
glowing_text(text2, -50)
pen.clear()

# --- Final steady text ---
pen.goto(0, 0)
pen.color("white")
pen.write("KELVIN MAINA says WANTAM", align="center", font=("Arial", 36, "bold"))

time.sleep(2)
pen.clear()
turtle.done()
