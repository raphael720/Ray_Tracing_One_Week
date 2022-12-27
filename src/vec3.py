import numpy as np

class Vec3(np.ndarray):

    def __new__(cls, a):
        obj = np.asarray(a).view(cls)
        return obj

    def squared_length(self):
        return np.dot(self, self)#(self[0]*self[0] + self[1]*self[1] + self[2]*self[2])

    def length(self):
        return np.sqrt(self.squared_length())
    
    def unit_vector(self):
        # self[0] = self[0]/self.length
        # self[1] = self[1]/self.length
        # self[2] = self[2]/self.length
        size = self.length()
        return Vec3([self[0]/size, self[1]/size, self[2]/size])
        