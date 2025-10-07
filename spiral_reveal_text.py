import turtle
import colorsys
import time

# --- Setup screen ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Spiral Reveal - KELVIN MAINA says WANTAM")
screen.tracer(0)

# --- Turtle setup ---
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.hideturtle()

# --- Text to reveal ---
message = "KELVIN MAINA says WANTAM"
radius = 10
angle = 0

# --- Spiral with rainbow color cycling ---
for i, char in enumerate(message):
    hue = (i / len(message)) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    screen.colormode(1.0)
    t.pencolor(r, g, b)
    
    # Draw small spiral segment
    t.forward(radius)
    t.right(20)
    radius += 2
    
    # Write next character
    t.penup()
    t.forward(20)
    t.write(char, align="center", font=("Courier", 20, "bold"))
    t.backward(20)
    t.pendown()
    
    screen.update()
    time.sleep(0.1)

# --- Final display ---
t.penup()
t.goto(0, -200)
t.pencolor("white")
t.write("🌈 Spiral Reveal Complete!", align="center", font=("Arial", 16, "italic"))

screen.update()
time.sleep(2)
turtle.done()
