import math
import os

from PIL import Image

def path_image(title:str, extension:str) -> str:
    path = os.path.join(os.path.dirname(__file__), '..', 'images', f'{title}.{extension}')


if __name__ == "__main__":
    # image
    title = 'image_0'
    image_colors = 'P3' # para o formato ppm
    image_width = 800
    image_height = 600

    if 'images' not in os.listdir(os.path.join(os.path.dirname(__file__), '..')):
        os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'images'))

    # PPM image
    
    file = open(path_image(title, 'ppm'), 'w')

    file.write(f'{image_colors}\n')
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

    #PNG image
    image_png = Image.new('RGB', (image_width, image_height))
    image_pixel = image_png.load()

    for j in range(0, image_height):
        for i in range(0, image_width):
            r = i / (image_width-1)
            g = 1 - j / (image_height-1)
            b = 0.25

            ir = int(255.99 * r)
            ig = int(255.99 * g)
            ib = int(255.99 * b)

            image_pixel[i, j] = (ir,ig,ib)


    image_png.save(path_image(title, 'png'), "PNG")
