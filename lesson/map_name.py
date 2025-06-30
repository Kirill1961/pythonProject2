
def before():
    return 'BEFORE MAIN'

def after():
    return 'AFTER MAIN'


print("Executed during import")


print(__name__, ' -> Имя импортируемого файла из переменной __name__ "До"')


# TODO  before() вызывается всегда, after() только при прямом вызове
print(before())
if __name__ == '__main__':
    print(after())
    print(__name__, ' -> Имя импортируемого файла из переменной __name__ "После"')

