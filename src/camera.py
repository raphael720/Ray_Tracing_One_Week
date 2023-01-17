from vec3 import Vec3
from ray import Ray

class Camera:
    def __init__(self) -> None:
        aspect_ratio = 16/9

        viewport_height = 2
        viewport_width = aspect_ratio * viewport_height
        focal_length = 1

        self.origin: Vec3 = Vec3([0,0,0])
        self.horizontal: Vec3 = Vec3([viewport_width, 0.0, 0.0])
        self.vertical: Vec3 = Vec3([0.0, viewport_height, 0.0])
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - Vec3([0.0, 0.0, focal_length])

    def get_ray(self, u: float, v: float) -> Ray:
        direction = self.lower_left_corner + u*self.horizontal + v*self.vertical - self.origin
        return Ray(self.origin, direction)
