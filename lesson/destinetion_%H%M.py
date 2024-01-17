import pprint
from datetime import datetime


def convert24_12(time24):
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
