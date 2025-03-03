import re

# TODO Простая регулярка, re.search ищет совпадения с pattern,
#  только подряд стоящие символы
# text = "I love exploring the planets of our solar system, especially jupiter."
text = "Kirill is a very good programmer and he will be fine, he also looks good."

pattern = r"will be fine"
res = re.search(pattern, text)
print(f"re.search -	Ищет первое совпадение в строке : < {res} > ", '\n')


pattern = r"Kirill"
res = re.match(pattern, text)
print(f"re.match - Проверяет, соответствует ли начало строки шаблону. : < {res} > ", '\n')


pattern = r"good"
res = re.findall(pattern, text)
print(f"re.findall - Возвращает список всех совпадений. : < {res} > ", '\n')


pattern = r"good"
res = re.finditer(pattern, text)
print(f"re.finditer - Возвращает итератор с объектами Match. : < {list(res)}> ", '\n')


res = re.sub('good', 'VERY good', text)
print(f"re.sub - Заменяет все совпадения на repl. : < {res}> ", '\n')


pattern = r" "
res = re.split(pattern, text)
print(f"re.split - Разбивает строку по шаблону.: < {res}> ", '\n')

pattern = r"Kirill is a very good programmer and he will be fine, he also looks good."
res = re.fullmatch(pattern, text)
print(f"re.fullmatch - Проверяет, соответствует ли вся строка шаблону.: < {res}> ", '\n')


pattern = r"will be fine, he also looks good."
res = re.compile(pattern)
print(f"re.compile - Компилирует шаблон для многократного использования.: < {res}> ", '\n')


# TODO Задача: извлечь корректные даты и телефоны
#  Костыли, Вывести Корректные Даты и телефоны
text_data = '''Сегодня на календаре 02/03/2025, а вчера было 01/03/2025.  
Встреча запланирована на 15/04/2024, а отчёт сдадим до 30/06/2023.  
Некорректные даты: 99/99/9999, 32/13/2025, 7/3/2024.  
Допустим, в логе есть 05/08/2020 и 25/12/2019.'''

phones = """+7 909-212-9930", "+3*9272160048", "7^999999a", +7 910-212-9930"7/920216/00/(48), 8 920-216-0048"""

# TODO Примитивная Регулярка
res = "".join(re.findall(r"\d+\W", text_data))
res1 = "".join(re.findall(r"[\d+/ ]", text_data))

print(res, '\n')
print([i for i in res1.split(" ") if i[0:2] < "32" and i[3:6] < "13" and i[7:] < "2025" and i != ""], '\n')

#  TODO Костыли, c помощью итерации удаляемых символов
res2 = []
for p in ".,":
    text_data = text_data.replace(p, " ")
data = text_data.split(" ")
for i in data:
    if i[0:2] < "32" and i[3:6] < "13" and i[7:] < "2025" and i != "":
        res2.append(i)
print(res2, '\n')

# TODO Правило: Для каждой цифры диапазон [0-9],
#  {4} - Фигурные скобки это кол-во повторов Цифры
res3 =re.findall(r'[0-9]{2}[^0-9][0-9]{2}[^0-9][0-9]{4}', text_data)
res4 =re.findall(r'\d{2}\W\d{2}\W\d{4}', text_data)
res5 =re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b', text_data)
print(res3, '\n')
print(res4, '\n')
print(res5, '\n')

# TODO Вывлд телефона
res6 = re.findall(r'(?:\+7|8) (?:9[012][09]-)(?:2[01][026]-)(?:\d{4})', phones)
res7 = re.findall(r'(?:\+7|8)[\s-]?(9\d{2})[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})', phones)
print((res6))
print((res7))
