import sys, re
from io import StringIO
import csv

print(len(sys.argv), ' len(sys.argv)')
print("Имя скрипта:", sys.argv[0])
print("Аргументы командной строки:", sys.argv[1:])

regex = sys.argv[1]
print(regex, ' regex ************')
for line in sys.stdin:
    print(line, ' line>>>>>>>>>>>>')
    print(sys.stdout.write(line), ' stdout.write(line)<<<<<<<<<<<<<<<<')
    if re.search(regex, line): sys.stdout.write(line)
    # try:
    #     sys.stdout = open('eek.txt', 'a')
    #     print(regex)
    # finally:
    #     # Закрываем file.txt
    #     sys.stdout.close()
    #     sys.stdout = sys.__stdout__
    count = 0
    for line in sys.stdin:
        count += 1
        print(count, ' count')
# if __name__ == '__main__':
#
#     foo = sys.stdin.readline()
    # print (l)




# stdout = sys.stdout
#
# try:
#     sys.stdout = open('c_s_v.csv', 'w')
#     print('tyuklk; ')
# finally:
#     # Закрываем file.txt
#     sys.stdout.close()
#     sys.stdout = stdout







# stdin_fileno = sys.stdin
#
#
# for line in stdin_fileno:
#     # Remove trailing newline characters using strip()
#     if 'exit' == line.strip():
#         print('Found exit. Terminating the program')
#         exit(0)
#     else:
#         print('Message from sys.stdin: ---> {} <---'.format(line))






# lines = ['123']
# for line in sys.stdin:
#     lines.append(line)
# print('записали ввод через stdin в список lines',lines)

