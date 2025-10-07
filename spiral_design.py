import turtle
import time
import cv2
import numpy as np
import colorsys
from PIL import ImageGrab  # for capturing frames

# --- Setup the screen ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)  # smoother animation

# --- Create turtles ---
t1 = turtle.Turtle()
t2 = turtle.Turtle()

for t in [t1, t2]:
    t.speed(0)
    t.width(3)
    t.hideturtle()

# --- OpenCV video setup ---
output_file = "rainbow_spiral_dynamic.mp4"
fps = 30
frame_size = (800, 600)
video_writer = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps, frame_size)

# --- Drawing animation ---
angle = 0
radius = 100
start_time = time.time()

for i in range(180):
    # --- Calculate rainbow colors using HSV ---
    hue1 = (i / 180) % 1.0   # color for turtle 1
    hue2 = ((i + 0.5) / 180) % 1.0  # color for turtle 2 (offset slightly)
    rgb1 = colorsys.hsv_to_rgb(hue1, 1, 1)
    rgb2 = colorsys.hsv_to_rgb(hue2, 1, 1)

    # Convert float RGB (0–1) to 0–255 and hex for turtle
    t1.color((rgb1[0], rgb1[1], rgb1[2]))
    t2.color((rgb2[0], rgb2[1], rgb2[2]))

    screen.update()
    t1.penup()
    t2.penup()
    t1.goto(0, 0)
    t2.goto(0, 0)
    t1.setheading(angle)
    t2.setheading(-angle)
    t1.pendown()
    t2.pendown()
    t1.circle(radius, 180)
    t2.circle(radius, 180)
    angle += 5
    radius -= 0.2

    # --- Capture frame for video ---
    img = ImageGrab.grab(bbox=(100, 100, 900, 700))  # adjust if needed
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video_writer.write(frame)

    time.sleep(0.02)

# --- Wrap up ---
video_writer.release()
print("✅ Dynamic rainbow animation complete! Video saved as rainbow_spiral_dynamic.mp4")

screen.mainloop()
