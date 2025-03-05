""" запись csv файла, import csv -> создаём переменные
со значением (name_1 = 'Cirill' .....), открываем ф-л 'c_s_v.csv'
с флагом 'w' и передаём открытый ф-л переменной fil,
Создаём объект wri_te, где передаём в параметр методу writer
из модуля csv, ф-л fil для записи в него data.Из получившегося
объекта wri_te вызываем метод writerow для записи data в строку.
writerow имеет 1 аргумент поэтому данные объеденяем в коллекцию:
список,кортеж и тд
Чтение из файлов (парсинг)"""
""" newline - необязательно, режим перевода строк. Варианты: None, '\n', '\r' и '\r\n'. 
Следует использовать только для текстовых файлов.
    delimiter — это литеральная строка, определяющая заполнитель, представляющий разделитель,
по умолчанию запятая
   .read - метод читающий весь ф-л в один приём, непосредственно из открытого файла
   .readline() читает одну целую строку из файла, непосредственно из открытого файла 
Конечный символ новой строки \n сохраняется в строке.
    .readlines() читает файловый объект построчно, непосредственно из открытого файла циклом for или
ставим 1 str arg, пока не достигнет конца файла EOF и возвращает список, содержащий строки файла.
    reader() - csv, ф-я модуля csv возвращает объект чтения,(в виде списка строк), читает из ОБ csv 
в котором будем перебирать строки циклом for (example - reader=csv.reader(f) )
    writer()- csv, только для создания объекта для записи,ф-я модуля csv возвращает ф-л csv, с преобразованными данными
в строки с разделителями для данного файлового объекта, 
    .writelines() записывает итерируюмую коллекцию строк, непосредственно в открытый файл с циклом  for  
или с одним строчным аргументом, вся запись в одну строку.
    .writerow() csv,запишет строку row в файловый объект, 
отформатированный в соответствии с текущим диалектом csv.Dialect.
    .writerows() csv, запишет все строки rows, которые должны находится в итерируемом объекте 
в файловый объект, отформатированный в соответствии с текущим диалектом csv.Dialect.
    .writeheader() - только csv.DictWriter(), Записывает строку с именами полей
     DictReader() - класс, модуля csv создает объект, который работает как обычный reader(),
(т.е. читаем и преобразуем в словарь),но отображает информацию в каждой строке в словаре dict, 
ключи которого задаются необязательным параметром fieldnames.
    DictWriter() - класс модуля csv создает объект, который работает как csv.writer(), 
но позволяет передавать строку с данными на запись как словарь,
 ключи которой задаются необязательным параметром fieldnames.
    extrasaction='ignore' или 'raise'- значение отсутствующего ключа имени поля
    restval='' - значение поля для лишних/отсутствующих заголовков"""
import csv
import glob

""" io.TextIOBase - Буферизованный текстовый поток поверх двоичного потока."""
""" __________________можно записать  в 'c_s_v.csv' готовый list,dict,tuple например такой как 
словарь name_dic, """

name_1 = 'Cirill'
name_2 = 'Sveta'
name_dict = {'Ylia': 'Andry'}
with open('c_s_v.csv', 'w') as fil:
    wri_te = csv.writer(fil, delimiter='+')  # создаём ОБ писатель wri_te котор преобр fil в строки с разделителями
    wri_te.writerow([name_dict, name_2, name_1])

with open('c_s_v.csv') as fil:
    print(fil.readline())  # читаем содержимое с помощью read, readline, readlines

""" можно изначально добавить в 'csv - файл' заголовки колонок example:
' name users' and ' addresses users',
затем через цикл for добавить data users.Предварительно создав список
 например назовём data_users из имён и адресов"""

""" _______________________________________Создаём csv-файл.
Сначала в файл записываем названия колонок, затем составляем список пользователей 
и вновь открываем файл и записываем с флагом "a" последовательность в виде list"""
with open('c_from_data.csv', 'w', newline='') as file:
    write = csv.writer(file, delimiter='*')  # создаём ОБ писатель with name 'write'
    write.writerow((' name users', ' addresses users'))  # с помощью метода writerow пишем строку в виде list, в ОБ
    # write, в котором открыт в режиме 'w'  ф-л 'c_from_data.csv'

data_users = [
    ['user1', 'address1'],
    ['user2', 'address2'],
    ['user3', 'address3'],
]
for data_u in data_users:
    with open('c_from_data.csv', 'w', newline='') as file_d:
        write_r = csv.writer(file_d, delimiter='*')  # создаём ОБ писатель with name write_r, преобр д/записи
        write_r.writerow(data_u)  # с помощью метода writerow берём строку из цикла (data_u) и пишем в ОБ write_r

with open('c_from_data.csv') as read_file:
    print(read_file.read())

with open('c_from_data.csv', 'r') as read_users:
    for read_us in csv.reader(read_users):
        print(read_us)

""" _____________________Запись с помощью writerows. Помещаем названия столбцов сразу в список"""

data_users = [
    (' name users', ' addresses users'),
    ['user1', 'address1'],
    ['user2', 'address2'],
    ['user3', 'address3'],
]

with open('c_from_data.csv', 'w', newline='') as file_d:
    write_r = csv.writer(file_d, delimiter=';')  # создаём ОБ писатель with name write_r
    write_r.writerows(data_users)  # writerows запишет все строки rows из коллекции

with open('c_from_data.csv', 'r') as read_users:
    for read_us in csv.reader(read_users):
        print(read_us)

with open('c_from_data.csv', newline='\n') as d_read_users:
    for dic_read in csv.DictReader(d_read_users):
        print(dic_read)

""" ________Добавляем в ф-л cdata расписание:c помощью for + .write ; for + .writerow ; .writerows; .writelines"""

time_dest = [['11:45', 'ROCK SOUND'],
             ['17:55', 'ROCK SOUND'],
             ]
with open('c_from_data.csv', 'a', newline='\n') as f:
    for id in time_dest:
        f.writelines(id)

with open('c_data.csv', 'w') as data:
    for i in time_dest:
        data.write(str(i))

with open('c_data.csv', 'w', newline='\n') as data:
    for i in time_dest:
        print(i)
        write = csv.writer(data)
        write.writerow(i)

with open('c_data.csv', 'w', newline='') as data:
    write = csv.writer(data)
    write.writerows(time_dest)

with open('c_data.csv') as data:
    print(data.read())

with open('c_data.csv') as data:
    for i_d in csv.reader(data):
        print(i_d)

""" ___________________________Добавка в csv с writerows, и чтение с DictReader"""

data_users = [

    ['Kirill', 'Voroneg', '13265987'],
    ['Sveta', 'Voroneg', '27895246'],
    ['Andrew', 'Voroneg', '33298744'],
]

with open('c_from_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)  # создаём ОБ писатель with name writer
    writer.writerows(data_users)
#
# with open('c_from_data.csv') as file:
#     red = csv.reader(file)
#     for i in red:
#         print(i)
#
with open('c_from_data.csv', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')  # создаём ОБ писатель with name writer
    for i in reader:
        print(i)

data_app = [['July', 'Mixico', '46522197'],
            ['Arty', 'Mexico', '52214983']
            ]

with open('c_from_data.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')  # создаём ОБ писатель with name writer
    writer.writerows(data_app)

""" _Запись и добавка в csv с DictWriter() из другого csv через цикл, так же заголовков полей c .writeheader()"""

with open('c_from_data.csv', 'r') as da_ta:
    # header = ['name users ', 'addresses users', 'Phone']
    reader = csv.DictReader(da_ta, fieldnames=['name users //', 'addresses users', 'Phone'], )
    with open('c_in_data.csv', 'w', newline='') as fi_le:
        writer = csv.DictWriter(fi_le, fieldnames=['name users //', 'addresses users', 'Phone'])
        writer.writeheader()  # запись ключей
        for i_dict in reader:
            # print(i_dict)
            writer.writerow(i_dict)
            print(i_dict)

""" Тоже самое читаем из 'c_from_data.csv' пишем в 'c_in_data.csv' но убираем одну колонку
    с помощью  del i_dict ['addresses users /']
    ВНИМАНИЕ! убрав колонку 'addresses users /' - fieldnames убирать можно только
     в записывающем блоке"""

with open('c_from_data.csv', 'r') as da_ta:
    # header = ['name users ', 'addresses users', 'Phone']
    reader = csv.DictReader(da_ta, fieldnames=['name users /', 'addresses users /', 'Phone'], )
    with open('c_in_data.csv', 'w', newline='') as fi_le:
        writer = csv.DictWriter(fi_le, fieldnames=['name users /', 'Phone'])
        writer.writeheader()  # заголовков
        for i_dict in reader:
            # print(i_dict)
            del i_dict['addresses users /']
            writer.writerow(i_dict)
            print(i_dict)
""" ________________________Простой способ записи csv в виде словаря"""

with open('c_s_v.csv', 'w', newline='') as fi_le:
    header = ['names', 'addresses', 'N_o']
    writer = csv.DictWriter(fi_le, fieldnames=header)  # создаём ОБ для записи в него + fieldnames
    writer.writeheader()  # запись имён полей
    writer.writerow({'names': 'user1', 'addresses': 'address1', 'N_o': '1'})
    writer.writerow({'names': 'user2', 'addresses': 'address2', 'N_o': '2'})

# TODO"""Использование restval= и extrasaction= """

with open('c_from_data.csv', 'r') as da_ta:
    reader = csv.DictReader(da_ta)
    with open('c_s_v.csv', 'w', newline='') as fi_le:
        header = ['names', 'addresses', 'N_o']
        writer = csv.DictWriter(fi_le, fieldnames=header, restval='I known', extrasaction='ignore')

        writer.writeheader()
        for i_dict in reader:
            print(i_dict)
            writer.writerow(i_dict)

directory = r"C:\Users\Kirill\PycharmProjects\pythonProject3\*"
file = glob.glob(directory)
print(file, ">>>>>>>>>>>>>>>")
# Чтение строки из файла и обработка

# with open('file.txt') as f:
#     while line := f.readline():
#         print(f"Прочитана строка: {line.strip()}")


# Функция для поиска файлов с нужным расширением
import glob


# Функция для поиска файлов с нужным расширением
def find_files(directory, extension):
    pattern = f'{directory}/**/*.{extension}'
    return glob.glob(pattern, recursive=True)


# Пример использования
directory = r"C:\Users\Kirill\PycharmProjects\pythonProject3\**"  # Текущий каталог
extension = 'txt'  # Искомое расширение
files = find_files(directory, extension)

print(files, " |||||||||||||||||||||||||")

# Читаем из txt и обрабатываем строки в своей директории
with open("text.txt") as files:
    while reader := files.readline():
        print(reader)