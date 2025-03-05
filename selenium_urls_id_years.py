import requests
from bs4 import BeautifulSoup

url = "https://e-disclosure.ru/portal/company.aspx?id=403"

headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-kl-ajax-request": "Ajax_Request",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://e-disclosure.ru/portal/company.aspx?id=401",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем input с id="EventsYears"
    events_years = soup.find("input", {"id": "EventsYears"})

    if events_years:
        years = events_years.get("value")  # Получаем значение атрибута "value"
        print("Доступные годы событий:", years)
    else:
        print("Элемент с id='EventsYears' не найден!")
else:
    print("Ошибка запроса:", response.status_code)
