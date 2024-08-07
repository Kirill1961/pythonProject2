import sys
from sys import exc_info, exception  # весь импорт должен быть в начале кода

""" Инструкция raise позволяет программисту:
-Принудительно вызвать одно исключение в любое время и в любом месте кода.
-Повторно вызвать исключение, которое было перехвачено try/except.
-Создавать исключения, когда выполнение программы бессмысленно или не может
продолжаться (например при вводе данных с клавиатуры).
ТК пайтон не может сгенерировать исключения на все случаи,
мы может это сделать сами с помощью raise, Exeption - это
 обобщённый класс для всех видов исключений"""
""" 
Исключения бывают разных типов и конкретный тип брошенного
исключения печатается до двоеточия. В данном случае это ZeroDivisionError.
После типа ошибки выводится дополнительная информация, которая может
зависеть от типа ошибки и причины её возникновения.
Всё, что идёт до последней строки, демонстрирует в каком контексте
возникла ошибка в виде трассировочных данных. Более наглядное представление о трассировочной
информации даёт пример, когда ошибка возникает внутри нескольких функций.
Исключение распространяется наверх по стеку вызовов, 
пока не встретится блок, обрабатывающий это исключение try/except. 
Если такой блок так и не встречается, то выводится сообщение об ошибке
и программа падает (или может продолжить ожидание инструкций от пользователя
в интерактивном режиме, что происходит, например, в jupyter ноутбуках).
"""
""" Функции которые возвращают данные об исключениях:
    sys.exc_info() - получает информации об исключении;
    sys.exception() - возвращает экземпляр исключения;
    sys.excepthook() - обработка необработанных исключений;
    sys.unraisablehook() обработка невыполнимых исключений;
    sys.exc_info() - возвращает кортеж из трех значений,
     которые предоставляют информацию об исключении, 
     которое в данный момент обрабатывается. 
     Возвращаемая информация относится как к текущему потоку, 
     так и к текущему кадру стека.
    exc_type получает тип обрабатываемого исключения;
    exc_value получает значение(экземпляр)исключения;
    exc_traceback отслеживание трассировка исключения.
    если исключение не возникло они = None"""

""" Создание исключения: оператор raise затем имя
класса исключения ZeroDivisionError, в скобках сообщение
 об ошибке"""
# print('Call Error')
# raise ZeroDivisionError('not error ZeroDivision')
# print ('work after error')


""" вызов исключения: можно создать экземпляр класса ZeroDivisionError
и после raise прописать этот экземпляр в виде переменной"""

# print('Call Error')
# e_rr = ZeroDivisionError('not error ZeroDivision')
# raise e_rr
# print ('work after error')


# raise  Exception ('my first ecxeption')


#
# def f():
#     print("До исключения!")
#     raise Exception("Исключение!")
#     print("После исключения!")
#
# f()


""" создали класс где объект er вызывает метод print(self, data)
  тот в свою очередь send_data(self, data) который проверяет
  на истинность send_to_print в случае False происходит 
  исключение """


class PrintData:

    def print(self, data):
        self.send_data(data)
        print(f"print: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exception("printer not answer")

    def send_to_print(self, data):
        return False  # если возвращаем False, то код видит что принтер данные не получил если True,
        # то видит что получил данные


er = PrintData()  # создали экземпляр "er" класса PrintData, затем обрабатываем
# возможное исключение вызова метода print из объекта "er".
try:
    er.print("123>>>>>>>>>>>>>>>")
except (
    Exception
) as err:  # через переменную err из класса Exception выводим наименование ошибки 'printer not answer'
    print(
        "all ok", err, exc_info()[0]
    )  # в [ ] указываем индекс значения из кортежа возвращаемого exc_info()
    # (type, value, traceback)
""" мы можем написать свой класс исключения
преимущество самописного класса в том что программист 
будет точно знать какое  исключение отлавливается,
в данном случае "не отправка принтером данных для печати
send_to_print """


class Exceptionsendtoprint(Exception):
    pass  # <---можно в теле класса ничего не выполнять


"""  a можно вывести коментарий для чего нужен класс"""


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"print: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise Exceptionsendtoprint("new klass Exceptionsendtoprint")

    def send_to_print(self, data):
        return False


er = PrintData()
try:
    er.print("123")
except Exceptionsendtoprint as ert:
    print(
        "this except:", ert, sys.exc_info()
    )  # если не указывать индекс в [ ], то вывод всех параметров


# scool and student
class Scool:
    free_seats = True
    remote = 2

    @property  # @property -  превращает метод scool_param в атрибут, можно вызывать без скобок
    def scool_param(self):
        if self.free_seats == True and self.remote < 5:
            return True
        return False


class Student:
    level = 5
    age = 20

    @property  # @property - превращает метод student_param  в атрибут, можно вызывать без скобок
    def student_param(self):
        if self.level > 3 and self.age < 12:
            return True
        return False


scl = Scool()
std = Student()

print(std.student_param)
print(scl.scool_param)

# if std.student_param and scl.scool_param:  # если используем @property то скобки у методов не ставим
#     print("Welcome")
# else:
#     print("not accepted")
# std.student_param()
# scl.scool_param()
