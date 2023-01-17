import os
from sys import maxsize

from numpy import random
from PIL import Image
from tqdm import tqdm

from vec3 import Vec3
from ray import Ray
from camera import Camera

from sphere import Sphere
from hittable import HitRecord
from hittable_list import HittableList

def clamp(x: float, float_min: float, float_max: float) -> float:
    if x < float_min: return float_min
    if x > float_max: return float_max
    return x

def ray_color(r: Ray, word: HittableList) -> Vec3:
    rec: HitRecord = HitRecord()
    if word.hit(r, 0, maxsize, rec):
        return 0.5 * (rec.normal + Vec3([1,1,1]))

    unit_direction = r.direct.unit_vector()
    t = 0.5*(unit_direction[1] + 1)
    return (1-t)*Vec3([1,1,1]) + t*Vec3([0.5,0.7,1.0])

def write_color(pixel_color: Vec3, samples_per_pixel: int) -> tuple[int, int, int]:
    scale = 1 / samples_per_pixel

    r = pixel_color[0] * scale
    g = pixel_color[1] * scale
    b = pixel_color[2] * scale

    ir = int(255.99 * clamp(r, 0.0, 0.9999))
    ig = int(255.99 * clamp(g, 0.0, 0.9999))
    ib = int(255.99 * clamp(b, 0.0, 0.9999))

    return (ir, ig, ib)

if __name__ == "__main__":

    if 'images' not in os.listdir(os.path.join(os.path.dirname(__file__), '..')):
        os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'images'))

    path_image = lambda title: os.path.join(os.path.dirname(__file__), '..', 'images', f'{title}.png')

    # Image
    title = 'image_6'
    aspect_ratio = 16/9
    image_width = 200 
    image_height = int(image_width / aspect_ratio)
    sample_per_pixel = 50

    # Word
    word: HittableList = HittableList()
    sphere1: Sphere = Sphere([0,0,-1], 0.5)
    sphere2: Sphere = Sphere([0,-100.5,-1], 100)
    word.add(sphere1)
    word.add(sphere2)

    # Camera
    cam: Camera = Camera()

    # Render
    print(f"Criando a {title} {image_width}x{image_height}")

    #PNG image
    image_png = Image.new('RGB', (image_width, image_height))
    image_pixel = image_png.load()

    for j in tqdm(range(0, image_height)):
        for i in range(0, image_width):
            pixel_color: Vec3 = Vec3([0.0,0.0,0.0])
            for s in range(0, sample_per_pixel):
                u = (i + random.rand()) / (image_width-1)
                v = 1 - (j + random.rand()) / (image_height-1)
                ray: Ray = cam.get_ray(u, v)
                pixel_color += ray_color(ray, word)

            image_pixel[i, j] = write_color(pixel_color, sample_per_pixel)


    image_png.save(path_image(title), "PNG")
