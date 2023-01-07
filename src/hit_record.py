from vec3 import Vec3
from ray import Ray

import numpy as np

class HitRecord:
    def __init__(self):
        self.point3 = None
        self.normal = None
        self.t = None
        self.front_face = None

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        self.front_face = np.dot(r.direct, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal 