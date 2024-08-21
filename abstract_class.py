from abc import ABC, abstractmethod

"""
Абстрактный класс
"""
# Создание абстрактного класса с использованием модуля abc
class Shape(ABC):

    # Абстрактный метод
    @abstractmethod
    def area(self):
        pass

    # Обычный метод, который может быть реализован в абстрактном классе
    def describe(self):
        return "I am a shape"


# Дочерний класс, который наследует абстрактный класс Shape
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    # Реализация абстрактного метода
    def area(self):
        return 3.14 * (self.radius ** 2)


# Попытка создать экземпляр абстрактного класса вызовет ошибку
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area

# Создание экземпляра класса Circle
circle = Circle(5)

# Вызов метода area() у экземпляра класса Circle
print(circle.area())  # Output: 78.5

# Вызов метода describe() у экземпляра класса Circle, унаследованного от абстрактного класса
print(circle.describe())  # Output: I am a shape

from abc import ABC, abstractmethod


# Создание абстрактного класса с использованием модуля abc
class Shape(ABC):

    # Абстрактный метод
    @abstractmethod
    def area(self):
        pass

    # Обычный метод, который может быть реализован в абстрактном классе
    def describe(self):
        return "I am a shape"


# Дочерний класс, который наследует абстрактный класс Shape
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    # Реализация абстрактного метода
    def area(self):
        return 3.14 * (self.radius ** 2)


# Попытка создать экземпляр абстрактного класса вызовет ошибку
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area

# Создание экземпляра класса Circle
circle = Circle(5)

# Вызов метода area() у экземпляра класса Circle
print(circle.area())  # Output: 78.5

# Вызов метода describe() у экземпляра класса Circle, унаследованного от абстрактного класса
print(circle.describe())  # Output: I am a shape

"""
Полиморфизм
"""
class Lexic:
  def __init__(self, code):
    self.code = code


class SQLLexic(Lexic):
  def delete_commands(self):
    self.code = self.code.replace('drop', '').replace('delete', '')

  def delete_imports(self):
    ...

  def delete_comments(self):
    self.code = self.code.replace('--', '')

  def process(self):
    self.delete_commands()
    self.delete_comments()

class MySQLLexic(SQLLexic):
    def delete_comments(self):
      self.code = self.code.replace('--', '')

class PythonLexic(Lexic):
  def delete_commands(self):
    self.code = self.code.replace('eval', '').replace('exec', '')

  def delete_imports(self):
    self.code = self.code.replace('import ', '')

  def process(self):
    self.delete_commands()
    self.delete_imports()


mycode = """
import os, sys
-- my comment
drop table

a = 1
eval(a)
"""

ex = PythonLexic(code=mycode)
ex.process()

print(ex.code)

d = {
    'Python': PythonLexic,
     'SQL': SQLLexic
}

def main(code, language):
  ex = d[language](code)
  ex.process()

  return ex.code
main (mycode, 'SQL')
