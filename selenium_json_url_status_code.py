import requests
from bs4 import BeautifulSoup

url_base = "https://e-disclosure.ru/"
# url = "https://e-disclosure.ru/portal/company.aspx?id="
# url = "https://e-disclosure.ru/api/events/page?companyId=402&year=2005"

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
    "referer": "https://e-disclosure.ru/portal/company.aspx?id=",  # Можно с любым id ....../company.aspx?id=401
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

# TODO Метод .json() в response.json() используется в requests,
#  чтобы преобразовать JSON-ответ сервера в Python-объект (обычно dict или list).



for id in range(401, 403):

    print(id)
    url_date = url_base + 'portal/company.aspx?id=' + str(id)  # url Предприятия c id = str(id)
    # print(url_date)
    url_date_events = url_base + 'api/events/page?companyId=' + str(id) + '&year='  # url для даты и события
    # print(url_date_events)

    response_html = requests.get(url_date, headers=headers)  # Запрос для html
    # print(response_html.status_code)

    response_json = requests.get(url_date_events, headers=headers)  # Запрос для json

    type_response_html = response_html.headers.get('Content-Type')
    # print(type_response_html)
    if 'text/html' in type_response_html:  # Проверяем response_html на text/html формат
        if response_html.status_code == 200:
            soup = BeautifulSoup(response_html.text, 'lxml')



            # TODO 'input' и {'id':"EventsYears"} - нашёл в html -> через Crtl + U
            years_events = soup.find('input', {'id':"EventsYears"})
            # print(years_events)

            # TODO Извлекаем только даты событий для монтировки url_events_years
            #  years_events - это словарь
            if years_events:

                # TODO Атрибуты тега 'input' находятся в BeautifulSoup в виде словаря
                # print(f'Атрибуты тега "input" это словарь -> {years_events.attrs}')
                # print(f"Даты по ключу value -> {years_events.get('value')}")

                years = years_events.get('value')  # Ключ value извлекает даты из словаря


                # TODO монтируем url для извлечения даты + события
                for year_event in years.split(','):  # Разделили даты, каждая дата - отдельная строка
                    url_events_years = url_date_events + str(year_event)  # url для события и даты
                    print(url_events_years, '>>')
                    response_event = requests.get(url_events_years, headers=headers)  # запрос по  url_events_years
                    type_response_event = response_json.headers.get('Content-Type')  # Определяем тип content от сервера
                    # print(type_response_event, '>')
                    if "application" in type_response_event:  # Проверяем ответ от сервера на json-формат
                        events = response_event.json()  # Преобразуем json-формат в py
                        for event in events:
                            print(f"Событие: {event['eventName']} Дата: {event['eventDate']}")
                    else:
                        print('content json-type doesnt match')
            else:
                print('Date Not Found')
        else:
            print('Error')
    else:
        print('content type doesnt match')