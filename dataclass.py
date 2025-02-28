from dataclasses import dataclass, asdict


# TODO Стандартное Создание класса
class Trench:
    def __init__(self, lenght, widht, depth):
        self.depth = depth
        self.lenght = lenght
        self.widht = widht

    def siz_trench(self, x, y, z):
        return x * y * z


trench_one = Trench(1, 2, 0.5)

print(trench_one.widht)
print(trench_one.siz_trench(1, 2, 0.5))


# TODO Создание класса с декоратором @dataclass
#  Автоматическое создание __init__
@dataclass
class Cube:
    lenght: int
    widht: int
    height: int

    def volume_cube(self,
                    x: int,
                    y: int,
                    z: int) -> int:
        return x * y * z


    def side_area(self):
        return self.widht * self.lenght


# TODO Создание ОБ
cube_one = Cube(1, 2, 5)
cube_two = Cube(50, 20, 70)
cube_three = Cube(1, 2, 5)


# TODO Преобразование в dict
dict_hole_one = asdict(cube_one)

# TODO обращение к методам
print(cube_one.volume_cube(5, 3, 2))
print(cube_two.side_area())

# TODO Вывод преобразованного словаря
print(dict_hole_one)

# TODO Автоматический __repr__ -> вывод инф. по объектам
print(cube_one, cube_two)

# TODO __eq__ -> Автоматическое сравнение  размеров двух кубов
print(cube_one == cube_three)