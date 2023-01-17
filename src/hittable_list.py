from ray import Ray
from hittable import HitRecord, Hittable

class HittableList(Hittable):
    def __init__(self, list_objects: list[Hittable] = None):
        if list_objects:
            self.objects: list[Hittable] = list_objects
        else:
            self.objects: list[Hittable] = list()

    def add(self, param_object: Hittable):
        self.objects.append(param_object)
    
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        tem_rec: HitRecord = HitRecord()
        hit_anything: bool = False
        closest_so_far = t_max

        for inte_object in self.objects:
            if inte_object.hit(r, t_min, closest_so_far, tem_rec):
                hit_anything = True
                closest_so_far = tem_rec.t

                rec.t = tem_rec.t
                rec.point3 = tem_rec.point3
                rec.normal = tem_rec.normal

        return hit_anything

