
def before():
    return 'BEFORE MAIN'

def after():
    return 'AFTER MAIN'


print("Executed during import")

# TODO  before() вызывается всегда, after() только при прямом вызове
print(before())
if __name__ == '__main__':
    print(after())


