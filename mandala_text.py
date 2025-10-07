import turtle
import colorsys
import time

# --- Screen setup ---
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.title("KELVIN MAINA says WANTAM - Ultimate Mandala 🌀")
screen.tracer(0)

# --- Create turtles ---
t1 = turtle.Turtle()
t2 = turtle.Turtle()
halo = turtle.Turtle()
text_turtle = turtle.Turtle()

for t in (t1, t2, halo):
    t.speed(0)
    t.width(2)
    t.hideturtle()

text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(0, -40)
text_turtle.color("white")

# --- Parameters ---
num_colors = 72
hue = 0
bg_hue = 0
angle = 0

# --- Mandala draw function ---
def draw_mandala(angle_offset):
    global hue
    for i in range(36):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t1.pencolor(color)
        t2.pencolor(color)
        hue += 1 / num_colors

        t1.circle(120)
        t1.right(10 + angle_offset)
        t1.forward(10)

        t2.circle(120)
        t2.left(10 + angle_offset)
        t2.forward(10)

# --- Halo glow function ---
def draw_halo(radius, intensity):
    halo.clear()
    color = colorsys.hsv_to_rgb(hue, 1, intensity)
    halo.pencolor(color)
    halo.penup()
    halo.goto(0, -radius)
    halo.pendown()
    halo.circle(radius)

# --- Glowing text intro ---
for glow in range(12):
    text_turtle.clear()
    scale = 1 + 0.03 * glow
    text_turtle.write("KELVIN MAINA says WANTAM",
                      align="center",
                      font=("Arial", int(26 * scale), "bold"))
    screen.update()
    time.sleep(0.08)

# --- Main animation loop ---
while True:
    # Dynamic background pulse
    bg_color = colorsys.hsv_to_rgb(bg_hue, 0.6, 0.2 + abs((bg_hue % 1) - 0.5))
    screen.bgcolor(bg_color)
    bg_hue += 0.002

    # Clear & redraw mandala
    t1.clear()
    t2.clear()
    draw_mandala(angle)
    angle += 1
    if angle > 360:
        angle = 0

    # Halo pulse
    draw_halo(150, 0.5 + 0.5 * abs((bg_hue * 2) % 1 - 0.5))

    # Text shimmer
    text_turtle.clear()
    text_turtle.color(colorsys.hsv_to_rgb(hue % 1, 1, 1))
    text_turtle.write("KELVIN MAINA says WANTAM",
                      align="center",
                      font=("Arial", 26, "bold"))

    screen.update()
    time.sleep(0.05)
