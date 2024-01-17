import sys, re

""" Дополнительные потоки stdin, stdout, stderr
    позволяют обмениваться данными между  OS и нашим кодом
    stdin - это поток из OS в наш код
    stdout - это поток из кода в OS"""


# reg = sys.argv[1:]
# for line in reg:
#     print(line)
#     # sys.stdout.read(str(line))
#     for i in sys.stdin:
#         print(i, ' sys.stdin')
#         sys.stdout.write(i)

""" Для конвеерной передачи пишем в cmd -
type .\eek.txt | py.exe .\a_stdin_youtube.py"""

# x = sys.stdin.read()
# # # x = sys.stdin.readlines()
# print(x)

no = 0
for line in sys.stdin: # читаем из txt файла и делаем форлуп forloop
    no += 1
    line = line.strip('')
    print(f'{no}' + '****' + line)