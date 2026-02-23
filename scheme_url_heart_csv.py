import requests

# URL файла
url = "https://raw.githubusercontent.com/GuySuphakit/Heart-Failure-Prediction/main/heart.csv"

# Скачивание файла
response = requests.get(url)

# Сохранение файла
with open("heart.csv", "wb") as file:

    file.write(response.content)

print("Файл успешно сохранён как heart.csv!")


# response = requests.get('https://e-disclosure.ru')

print(response.status_code)  # Выводит статус-код ответа
print(response.headers)  # Выводит заголовки ответа
# print(response.text)  # Выводит тело ответа в виде текста, если вы хотите получить содержимое веб-страницы, вы можете использовать

