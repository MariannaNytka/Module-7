class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @staticmethod
    def check(value):
        if type(value) is int or type(value) is float:
            return value
        else:
            return None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = self.check(value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = self.check(value)

# Приклад використання
point = Point("a", 10)
print(point.x)  # None
print(point.y)  # 10