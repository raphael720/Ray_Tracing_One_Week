import os
from sys import maxsize

from PIL import Image

from vec3 import Vec3
from ray import Ray
from sphere import Sphere
from hittable import HitRecord
from hittable_list import HittableList

def ray_color(r: Ray, word: HittableList) -> Vec3:
    rec: HitRecord = HitRecord()
    if word.hit(r, 0, maxsize, rec):
        return 0.5 * (rec.normal + Vec3([1,1,1]))

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
    title = 'image_4'
    aspect_ratio = 16/9
    image_width = 800 
    image_height = int(image_width / aspect_ratio)

    # Word
    word: HittableList = HittableList()
    sphere1: Sphere = Sphere([0,0,-1], 0.5)
    sphere2: Sphere = Sphere([0,-100.5,-1], 100)
    word.add(sphere1)
    word.add(sphere2)

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
            color: Vec3 = ray_color(ray, word)

            image_pixel[i, j] = write_color(color)


    image_png.save(path_image(title), "PNG")
