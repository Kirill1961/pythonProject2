

class C:
    def __init__(self, x):
        self.__x = x
    def get_x(self):
        return self.__x

# аргумент Х в def.set_x задаётся при вызове метода c.set_x(111)
    def set_x(self, x):
        self.__x = x
        print(self.__x)
c = C(5)
c.set_x(111)
print(c.get_x())


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

# Использование:
rect = Rectangle(10, 20)

# Доступ к свойствам
print(rect.width)  # 10
print(rect.height)  # 20
print(rect.area)  # 200

# Изменение ширины и высоты
rect.width = 15
rect.height = 25

print(rect.area)  # 375

# Попытка установить недопустимое значение
try:
    rect.width = -5
except ValueError as e:
    print(e)  # Width must be positive
