import math
import os

import numpy as np
from PIL import Image

from vec3 import Vec3
from ray import Ray

def hit_sphere(center:Vec3, radius:float, ray:Ray) -> float:
    origin_center = ray.orig - center
    a = np.dot(ray.direct, ray.direct)
    b = 2 * np.dot(origin_center, ray.direct)
    c = np.dot(origin_center, origin_center) - radius**2
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return -1.0
    else:
        return (-b - np.sqrt(discriminant)) / (2*a)


def ray_color(r: Ray) -> Vec3:
    t = hit_sphere(center=Vec3([0,0,-1]), radius=0.5, ray=r)
    if t > 0:
        n: Vec3 = (r.at(t) - Vec3([0,0,-1]))
        n = n.unit_vector()
        return 0.5*Vec3([n[0]+1, n[1]+1, n[2]+1])

    unit_direction = r.direct.unit_vector()
    t = 0.5*(unit_direction[1] + 1)
    return (1-t)*Vec3([1,1,1]) + t*Vec3([0.5,0.7,1.0])

def write_color(pixel_color: Vec3) -> tuple[int]:
    ir = int(255.99 * pixel_color[0])
    ig = int(255.99 * pixel_color[1])
    ib = int(255.99 * pixel_color[2])

    return (ir, ig, ib)

if __name__ == "__main__":

    if 'images' not in os.listdir(os.path.join(os.path.dirname(__file__), '..')):
        os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'images'))

    path_image = lambda title: os.path.join(os.path.dirname(__file__), '..', 'images', f'{title}.png')

    # Image
    title = 'image_3'
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
    print(f"Criando a imagem {image_width}x{image_height}")

    #PNG image
    image_png = Image.new('RGB', (image_width, image_height))
    image_pixel = image_png.load()

    for j in range(0, image_height):
        for i in range(0, image_width):
            u = i / (image_width-1)
            v = 1 - j / (image_height-1)
            direction = lower_left_corner + u*horizontal + v*vertical - origin
            ray: Ray = Ray(origin, direction)
            color: Vec3 = ray_color(ray)

            image_pixel[i, j] = write_color(color)


    image_png.save(path_image(title), "PNG")
