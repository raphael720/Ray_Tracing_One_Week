import math
import os

import numpy as np
from PIL import Image

from vec3 import Vec3
from ray import Ray

def hit_sphere(center:Vec3, radius:float, ray:Ray):
    origin_center = ray.orig - center
    a = np.dot(ray.direct, ray.direct)
    b = 2 * np.dot(origin_center, ray.direct)
    c = np.dot(origin_center, origin_center) - radius**2
    discriminant = b**2 - 4*a*c
    return discriminant > 0


def ray_color(r: Ray) -> Vec3:
    if hit_sphere(center=Vec3([0,0,-1]), radius=0.5, ray=r):
        return Vec3([1,0,0])

    unit_direction = r.direct.unit_vector()
    t = 0.5*(unit_direction[1] + 1)
    return (1-t)*Vec3([1,1,1]) + t*Vec3([0.5,0.7,1.0])

def write_color(file_out, pixel_color: Vec3, flag:str=None):
    ir = int(255.99 * pixel_color[0])
    ig = int(255.99 * pixel_color[1])
    ib = int(255.99 * pixel_color[2])

    if flag == "png":
        return (ir, ig, ib)
    else:
        file_out.write(f'{ir} {ig} {ib}\n')
    

def path_image(title:str, extension:str) -> str:
    return os.path.join(os.path.dirname(__file__), '..', 'images', f'{title}.{extension}')


if __name__ == "__main__":

    if 'images' not in os.listdir(os.path.join(os.path.dirname(__file__), '..')):
        os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'images'))

    # Image
    title = 'image_2'
    image_colors = 'P3' # para o formato ppm
    aspect_ratio = 16/9
    image_width = 800
    image_height = int(image_width / aspect_ratio)

    # Camera
    viewport_height = 2
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1

    origin: Vec3 = Vec3([0,0,0])
    horizontal: Vec3 = Vec3([viewport_width, 0.0, 0.0])
    vertical: Vec3 = Vec3([0.0, viewport_height, 0.0])
    lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3([0.0, 0.0, focal_length])

    # Render

    # PPM image
    file = open(path_image(title, 'ppm'), 'w')

    file.write(f'{image_colors}\n')
    file.write(f'{image_width} {image_height}\n')
    file.write('255\n')

    for j in range(image_height-1, -1, -1):
        for i in range(0, image_width):
            u = i / (image_width-1)
            v = j / (image_height-1)

            ray: Ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
            color: Vec3 = ray_color(ray)

            write_color(file, color)

    file.close()

    #PNG image
    image_png = Image.new('RGB', (image_width, image_height))
    image_pixel = image_png.load()

    for j in range(0, image_height):
        for i in range(0, image_width):
            u = i / (image_width-1)
            v = 1 - j / (image_height-1)
            ray: Ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
            color: Vec3 = ray_color(ray)

            image_pixel[i, j] = write_color(image_pixel, color, 'png')


    image_png.save(path_image(title, 'png'), "PNG")
