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
dict_hole_two = asdict(cube_two)

# TODO обращение к методам
print('обращение к методу volume_cube : \n', cube_one.volume_cube(5, 3, 2))
print('обращение к методу side_area : \n', cube_two.side_area(), '\n')

# TODO Вывод преобразованного словаря
print('asdict -> Преобразование в словарь :\n', dict_hole_two, '\n')

# TODO Автоматический __repr__ -> вывод инф. по объектам
print('Автоматический __repr__ -> вывод инф. по объектам : \n', cube_one, cube_two, '\n')

# TODO __eq__ -> Автоматическое сравнение  размеров двух кубов
print('Автоматическое сравнение  размеров двух кубов : \n', cube_one == cube_three)