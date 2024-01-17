class my:
    def __init__(self, name='Andr'):
        self.name = name

    def __repr__(self):
        return f'good people {self.name}'  # для именования переменных в коде для разработчиков увидим только в консоли

    def __str__(self):
        return f'very very good man {self.name} ' # для именования переменных при выводе для пользователя
p = my('Kirill')
print(p.name)
print(p)

