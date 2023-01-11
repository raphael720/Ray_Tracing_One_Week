from vec3 import Vec3
from ray import Ray
from hittable import HitRecord, Hittable

import numpy as np

class Sphere(Hittable):
    def __init__(self, center: Vec3, radius: float):
        self.center = center
        self.radius = radius
    
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        origin_center: Vec3 = r.orig - self.center
        a = r.direct.squared_length()
        haf_b = np.dot(origin_center, r.direct)
        c = origin_center.squared_length() - self.radius**2

        discriminant = haf_b**2 - a*c
        if discriminant < 0:
            return False
        discriminant_sqrt = np.sqrt(discriminant)

        # verifcando se as raizes, equação do segundo grau, está fora do range estabelecido
        root = (-haf_b - discriminant_sqrt) / a
        if root < t_min or root > t_max:
            root = (-haf_b + discriminant_sqrt) / a
            if root < t_min or root > t_max:
                return False

        rec.t = root
        rec.point3 = r.at(rec.t)
        outward_normal = (rec.point3 - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        return True

        

        
