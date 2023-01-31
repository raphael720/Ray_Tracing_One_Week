from numpy import sqrt, dot, asarray, ndarray, random # verficar de essa alteração deu certo

class Vec3(ndarray):

    def __new__(cls, a):
        obj = asarray(a).view(cls)
        return obj

    def squared_length(self):
        return dot(self, self)#(self[0]*self[0] + self[1]*self[1] + self[2]*self[2])

    def length(self):
        return sqrt(self.squared_length())
    
    def unit_vector(self):
        size = self.length()
        return Vec3([self[0]/size, self[1]/size, self[2]/size])

    @staticmethod
    def vec_random():
        return Vec3([random.rand(), random.rand(), random.rand()])

        