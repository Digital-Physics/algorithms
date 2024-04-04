#Torsion Angle: The torsion angle, also known as the twist angle, is the angle of rotation between two planes 
# torque is the rotational force
import math
# import numpy as np

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        """this overloads the - operator to handle Points class"""
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        """dot product, which is used in linear algebra matrix multiplication is like sumproduct in excel"""
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        """cross product is between two vectors in 3-d space. The two vectors define a plane and 
        the cross product is perpendicular to the plane. think thumb with pointer as vector a and middle as vector b"""
        # arr = np.cross(np.array([self.x, self.y, self.z]), np.array([no.x, no.y, no.z]))
        # return Points(arr[0], arr[1], arr[2])
        # c = a × b = (a2b3 - a3b2)i + (a3b1 - a1b3)j + (a1b2 - a2b1)k
        a1, a2, a3 = self.x, self.y, self.z
        b1, b2, b3 = no.x, no.y, no.z
        return Points(a2*b3 -a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)

    def absolute(self):
        """magnitude or distance from the origin in 3-d space"""
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))