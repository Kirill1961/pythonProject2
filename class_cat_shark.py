""" Переменные класса и переменные экземпляра"""

class Shark:
    """ Переменные класса"""
    animal_type = "fish"
    location = "ocean"

    """ Метод-конструктор с переменными экземпляра name и age"""
    def __init__(self, name = "Jhonn", age = 20):
        self.name = name
        self.age = age

    # Метод с переменной экземпляра followers
    def set_followers(self, followers):
        stive_name = self.name
        stive_age = self.age
        print("This user has " + str(followers) + " followers")
        print('Data this shark :' + 'name - ' + stive_name + ',' + 'age -' + f'{stive_age}')

Boop = Shark()
print(Boop.age, Boop.name, Boop.location, Boop.animal_type, Boop.name,'вызов переменных через ЭКЗ из класса')

    # print(animal_type,'/////////////////')
def main():
    """# Первый экземпляр. Установка переменных экземпляра метода-конструктора """
    sammy = Shark("Sammy", 5)

    # Вывод переменной экземпляра sammy
    print(sammy.name, sammy.age, '-> sammy.name + age')

    # Вывод переменной класса location
    print(sammy.location, '-> sammy.location')

    """# Второй экземпляр"""

    stevie = Shark("Stevie", 8)

    # Вывод переменной экземпляра name
    print(stevie.name, '-> stevie.name')

    # Использование метода set_followers и передача переменной экземпляра followers
    stevie.set_followers(77)

    # Вывод переменной класса animal_type
    print(stevie.animal_type, ' -> stevie.animal_type')

    print(sammy.animal_type, '|||||||||||||||||', Shark.animal_type)
    print(dir(sammy))
if __name__ == "__main__":
    main()











