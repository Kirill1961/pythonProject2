import requests
import tkinter as tk

# TODO User-Agent Многие веб-сайты блокируют запросы, которые не имеют заголовка User-Agent, добавим headers=headers
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



# response = requests.get('https://e-disclosure.ru/portal/company.aspx?id=29792', headers=headers )
# response = requests.get('https://www.example.com')
response = requests.get('https://www.google.com')

print(response.status_code)  # Выводит статус-код ответа
print(response.headers)  # Выводит заголовки ответа
print(response.text)  # Выводит тело ответа в виде текста, если вы хотите получить содержимое веб-страницы, вы можете использовать

# TODO Вывод ограниченного числа Символов html
# print(response.text[:10000])




# Создаём главное окно
root = tk.Tk()
root.title("Моё первое окно")  # Заголовок окна
root.geometry("300x200")  # Размер окна (ширина x высота)

# Добавляем кнопку
btn = tk.Button(root, text="Нажми меня", command=lambda: print("Кнопка нажата!"))
btn.pack(pady=20)  # Размещаем кнопку в окне

# Запуск главного цикла
root.mainloop()
