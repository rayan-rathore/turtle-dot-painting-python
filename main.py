import turtle
from datetime import datetime
import colorgram
from turtle import Turtle, Screen
import random



turtle.colormode(255)

"""colors = colorgram.extract("image.jpg", 30)
rgb_colors = []
for color in colors:
    cl = color.rgb.r, color.rgb.g, color.rgb.b
    rgb_colors.append(cl)

print(colors)
print(rgb_colors)
"""

aqua = Turtle()

aqua.hideturtle()
aqua.shape()
aqua.penup()
aqua.goto(-600,400)
colors = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49),
         (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31),
         (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
         (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

aqua.speed("fastest")
raw_x = -600
raw_y = 400
for y in range(15):
    aqua.goto(raw_x, (raw_y - (y* 50)))

    for _ in range(27):
        aqua.dot(20, random.choice(colors))
        aqua.forward(50)


screen = Screen()
aqua.getscreen()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screen.getcanvas().postscript(file = f"painting_{timestamp}.eps")
screen.exitonclick()