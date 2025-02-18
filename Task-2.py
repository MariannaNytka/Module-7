class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

# Приклад використання
point = Point(5, 10)

print(point.x)  # Виведе: 5
print(point.y)  # Виведе: 10

# Зміна значень через сеттери
point.x = 15
point.y = 20

print(point.x)  # Виведе: 15
print(point.y)  # Виведе: 20