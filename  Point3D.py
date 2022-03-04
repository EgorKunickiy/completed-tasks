from math import pow, sqrt


class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    @property
    def get_z(self):
        return self.__z

    def find_the_distance(self, point):
        return sqrt(pow(self.__x - point.get_x, 2)+pow(self.__y - point.get_y, 2)+pow(self.__z - point.get_z, 2))

    def __repr__(self):
        return '({}, {}, {})'.format(self.__x, self.__y, self.__z)

if __name__ == "__main__":
    point_1 = Point3D(1, 2, 3)
    print(repr(point_1))
    print(point_1.get_x)
    point_2 = Point3D(3, 4, 6)
    print(point_1.find_the_distance(point_2))
