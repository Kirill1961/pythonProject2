import requests

url = 'https://api.hh.ru/vacancies'

headers = {
    'HH-User-Agent': 'tg_vacancy_parser/1.0 (demorest@mail.ru)'
}

params = {
    'text': 'Data Scientist',
    'per_page': 5
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

# response.raise_for_status()
#
# data = response.json()

# print(data)

print(response.status_code)
print(response.text)