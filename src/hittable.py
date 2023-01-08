from abc import ABC, abstractclassmethod

import numpy as np

from vec3 import Vec3
from ray import Ray

class HitRecord:
    def __init__(self):
        self.point3 = None
        self.normal = None
        self.t = None
        self.front_face = None

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        self.front_face = np.dot(r.direct, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal 

class Hittable(ABC):
    @abstractclassmethod
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        pass
