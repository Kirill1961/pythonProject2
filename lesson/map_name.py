
def before():
    return 'ПРИ ПРЯМОМ ЗАПУСКЕ ЗАПУСКАЕТСЯ ВЕСЬ КОД в тч BEFORE MAIN'

def after():
    return 'ПРИ ПРЯМОМ ЗАПУСКЕ ЗАПУСКАЕТСЯ ВЕСЬ КОД в тч AFTER'

print(after())

print("Executed during import")


print(__name__, ' -> Имя импортируемого файла из переменной __name__ "До"')


# TODO  before() вызывается всегда, after() только при прямом вызове
print(before())
if __name__ == '__main__':
    print(after())
    print(__name__, ' -> Имя импортируемого файла из переменной __name__ "После"')

