class Per:
    # атрибуты класса
    name = ""
    age = 0

    # атрибуты экземпляров
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


# Синтаксис такой
# Leo = Per("Leo", 10)

# или Синтаксис такой
Leo = Per()
Leo.name = "Leo"
Leo.age = 10

Bim = Per()
Bim.name = "Bim"
Bim.age = 25

Kir = Per()
Kir.name = "Kir"
Kir.age = 53

# список экземпляров
lst = [Leo, Bim, Kir]

# фильтр по атрибутам экземпляров
lst.sort(key=lambda x: x.name)
lst.sort(key=lambda x: x.age)

sort_name = [pers.name for pers in lst]
print(sort_name)
sort_age = [pers.age for pers in lst]
print(sort_age)

