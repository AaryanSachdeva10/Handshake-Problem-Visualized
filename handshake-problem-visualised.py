# Created by Aaryan Sachdeva 5 May 2024

from PIL import Image, ImageDraw
import math

diameter = 2000 
people = 20 # amount of people handshaking (points on circle)

radius = diameter / 2

color = 'black'

img = Image.new('RGB', (diameter, diameter), 'white')

draw = ImageDraw.Draw(img)

draw.ellipse([(0, 0),(diameter, diameter)], outline=color)

circumference = math.pi*diameter

center_angle = 360/people # in degrees

arc_length = circumference * (center_angle/360)

for start_point in range(1, people+1):
    x1 = radius + radius * math.sin((start_point*arc_length)/radius)
    y1 = radius - radius * math.cos((start_point*arc_length)/radius)

    for end_point in range(1, people):
        x2 = radius + radius * math.sin((end_point*arc_length)/radius)
        y2 = radius - radius * math.cos((end_point*arc_length)/radius)

        draw.line([(x1, y1), (x2, y2)], fill=color)

# formula for amount of handshakes is n(n-1)/2
print("Handshakes occured (lines): " + str(people*(people-1)/2))

img.show()