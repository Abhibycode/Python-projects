import random
import turtle

angles = [90, -90]
colors = ["maroon", "brown", "olive", "teal", "navy", "black", "red", "orange", "yellow", "lime", "green", "cyan", "blue", "purple", "magenta", "grey", "pink", "lavender", "coral", "indigo"]
sizes = range(3, 6)

screen = turtle.Screen()
screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

reel_aspect_ratio = 9 / 16
reel_height_pixels = 300
reel_width_pixels = int(reel_height_pixels * reel_aspect_ratio)
turtle.bgcolor("black")

for _ in range(100):
    turtle.forward(50)
    turtle.pensize(random.choice(sizes))
    turtle.left(random.choice(angles))
    turtle.color(random.choice(colors))

    x, y = turtle.position()

    if x > screen_width -20 or x < -screen_height +20 or y > screen_height - 20 or y < -screen_height +20:
        turtle.left(180)

turtle.exitonclick()