from math import pow, sqrt


class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def find_the_distance(self, point: 'Point3D'):
        return sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2) + pow(self.z - point.z, 2))

    def __repr__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

if __name__ == "__main__":
    point_1 = Point3D(1, 2, 3)
    print(repr(point_1))
    point_2 = Point3D(3, 4, 6)
    print(point_1.find_the_distance(point_2))
