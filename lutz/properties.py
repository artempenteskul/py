class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print('Getting radius...')
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            print('Setting radius...')
            self._radius = value
        else:
            raise ValueError('Radius cannot be negative.')

    @radius.deleter
    def radius(self):
        print('Deleting radius...')
        del self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2


if __name__ == '__main__':
    circle = Circle(5)

    print(circle.radius)

    circle.radius = 7

    print(circle.radius)

    print(circle.area)

    del circle.radius
