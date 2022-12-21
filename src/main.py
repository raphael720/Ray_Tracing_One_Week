import math
import os

# image
image_colors = 'P3'
image_width = 256
image_height = 256

if 'images' not in os.listdir(os.path.join(os.path.dirname(__file__), '..')):
    os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'images'))

path_image = lambda title: os.path.join(os.path.dirname(__file__), '..', 'images', f'{title}.ppm')

# PPM image
title = 'image_0'
file = open(path_image(title), 'w')

file.write(f'{title}\n')
file.write(f'{image_width} {image_height}\n')
file.write('255\n')

for j in range(image_height-1, -1, -1):
    for i in range(0, image_width):
        r = i / (image_width-1)
        g = j / (image_height-1)
        b = 0.25

        ir = int(255.99 * r)
        ig = int(255.99 * g)
        ib = int(255.99 * b)

        file.write(f'{ir} {ig} {ib}\n')

file.close()
