import pprint
from datetime import date, datetime, timedelta
import pytz
import time


"""date - конвертирует из объекта даты - строку НО из строки объект нельзя.
datetime - конвертирует из строки объект дату"""

def convert24_12(time24):
    print(time24)

    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('dest_%.csv', 'r') as file:
    ignor = file.readline()
    flights = {}
    for line in file:
        k, v = line.strip().split(',')
        flights[k] = v
        flights2 = {}
for k, v in flights.items():  # items очищает словарь от кавычек и скобок, извлекает из словаря key и value
    flights2[convert24_12(k)] = v.title()
pprint.pprint(flights2)

pprint.pprint({dst: [k for k, v in flights2.items() if dst == v] for dst in flights2.values()})

"""date"""
# date - конвертирует из объекта даты - строку НО из строки объект нельзя.
dt = date(2021, 11, 19)

# Делаем из этой даты строку
print(dt.strftime("%d / %m / %Y"))

# вытаскиваем любые параметры
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())

# Получаем сегодняшнюю дату
print(dt.today().year)


"""datetime"""
# datetime - конвертирует из строки объект дату
dtm = datetime(2021, 11, 19, 20, 15, 13, 283).strftime('%d   %m-%Y')
print(dtm)

# Делаем из строки дату
s = '2024-07-31 19:09'
print(datetime.strptime(s, '%Y-%m-%d %H:%M'))

# конвертируем datetime в date
print(datetime.strptime(s, '%Y-%m-%d %H:%M').date())


# Формат timestamp
# Даты и метки времени, метки времени - кол-во секунд с начала ЭПОХИ(01 01 1970)
s = '2022-11-15 19:09'
dt = datetime.strptime(s, '%Y-%m-%d %H:%M')
ts = datetime.timestamp(dt)
print(ts, "strptime")

# Первод обратно метки времени в дату
print(f"Обратный перевод из метки времени в дату : {datetime.fromtimestamp(ts)}")

# pytz.all_timezones - Временные пояса
all_time = pytz.all_timezones

# Конструктор часового пояса
time_Mosk = pytz.timezone('Europe/Moscow')
print(time_Mosk)

# данный вывод -  None тк tzinfo ищет часовой пояс но мы его не обозначили
print(datetime(2022, 11, 19, 23, 15, 16, 125).tzinfo, "- tzinfo ищет часовой пояс но мы его не обозначили")
dt = datetime(2022, 11, 19, 23, 15, 16, 125, time_Mosk)
print(dt.tzinfo, " -аргумент pytz.timezone('Europe/Moscow') добавлен")


# Считаем разность дат
dt = datetime(2022, 11, 19, 23, 15, 16, 125)
print(datetime.now() - dt, "Разность дат")
print(dt + timedelta(days=30), "Сложение дат")

# Разница в секундах
diff = datetime.now() - dt
print(diff.total_seconds() / 60 / 60, "Разница в секундах")

# Модуль time - например для замера времени работы кода
start = time.time() # time.time()- текущая дата в секундах

print('Hello')

time.sleep(2)  # приостановка, время останова в аргументе

print('Good')

print(f'Итоговое время: {time.time() - start} sec')