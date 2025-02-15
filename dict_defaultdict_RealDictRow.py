

"""
Преобразования Словарей и Словароподобных Объектов
"""

from collections import defaultdict

# Инициал-ия словаря где value пустые списки
d = defaultdict(list)
a = [d[_] for _ in "qwer"]
print(f"Values Пустые Списки {a}")
print(f"Инициал-й Словарь {d}")

# Инициал-ия словаря c заполнением списков value
d1 = defaultdict(list)
d1_apnd = [d1[j].append(i) for i, j in enumerate("asdf")]
print(f"Словароподобный ОБ {d1}")
print(f"Словароподобный ОБ Преобр в Список Кортежей тк items это ключи+значения {list(d1.items())}")
print(f"Словароподобный ОБ Преобр в Кореж Кортежей тк items это ключи+значения {tuple(d1.items())}")
print(f"Словароподобный ОБ Преобр в Список Списков с values {list(d1.values())}")
print(f"Словароподобный ОБ Преобр в Кортеж Списков с values {tuple(d1.values())}")
print(f"Словароподобный ОБ Преобр в Список Кортежей с values {[tuple(i) for i in d1.values()]}")
print(f"Словароподобный ОБ Преобр в Список Кортежей Списков с values {[(i,) for i in d1.values()]}")
print(f"Словароподобный ОБ Преобр в Список Списков с keys {list(d1.keys())}")

