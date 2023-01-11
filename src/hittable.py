from abc import ABC, abstractclassmethod

from numpy import dot

from vec3 import Vec3
from ray import Ray

class HitRecord:
    def __init__(self):
        self.point3 = None
        self.normal = None
        self.t = None
        self.front_face = None

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        self.front_face = dot(r.direct, outward_normal) < 0 # ou seja, se ele apontar para fora da esfera
        # se isso não acontecer ele vai retornar o outward, só que com o sentido inverso
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable(ABC):
    @abstractclassmethod
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        pass
