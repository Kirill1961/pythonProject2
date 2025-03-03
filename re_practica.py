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


# TODO Вывести Корректные Даты
text_data = '''Сегодня на календаре 02/03/2025, а вчера было 01/03/2025.  
Встреча запланирована на 15/04/2024, а отчёт сдадим до 30/06/2023.  
Некорректные даты: 99/99/9999, 32/13/2025, 7/3/2024.  
Допустим, в логе есть 05/08/2020 и 25/12/2019.'''

res = "".join(re.findall(r"\d+\W", text_data))
res1 = "".join(re.findall(r"[\d+/ ]", text_data))
print(res)
print([i for i in res1.split(" ") if i[0:2] < "32" and i[3:6] < "13" and i[7:] < "2025" and i != ""])

def data(x):
    for p in ".,":
        x = x.replace(p, " ")
        data = x.split(" ")
        print(data, ">>>>")
        for i in data:

            if i[0:2] < "32" and i[3:6] < "13" and i[7:] < "2025" and i != "":
                return i

    return x
print(data(res))