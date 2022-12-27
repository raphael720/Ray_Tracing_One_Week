from vec3 import Vec3

class Ray:
    def __init__(self, origin: Vec3, direction: Vec3) -> None:
        self.orig = origin
        self.direct = direction

    def at(self, t: float) -> Vec3:
        return self.orig + t*self.direct
