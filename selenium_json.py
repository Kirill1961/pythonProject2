import requests

url = "https://e-disclosure.ru/api/events/page?companyId=402&year=2005"

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
    try:
        data = response.json()
        print(data, 'n')
        for event in data:
            print(f"Событие: {event['eventName']}, Дата: {event['eventDate']}")
    except requests.exceptions.JSONDecodeError:
        print("Ошибка: сервер вернул не JSON.")
        print("Ответ сервера:", response.text[:500])  # Показываем часть ответа для отладки
else:
    print("Ошибка запроса:", response.status_code)
