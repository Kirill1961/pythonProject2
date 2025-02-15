import requests

# URL файла
url = "https://raw.githubusercontent.com/GuySuphakit/Heart-Failure-Prediction/main/heart.csv"

# Скачивание файла
response = requests.get(url)

# Сохранение файла
with open("heart.csv", "wb") as file:
    file.write(response.content)

print("Файл успешно сохранён как heart.csv!")
