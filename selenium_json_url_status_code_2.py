import requests
from bs4 import BeautifulSoup

url_base = "https://e-disclosure.ru/"

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
    "referer": "https://e-disclosure.ru/portal/company.aspx?id=",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

def get_html(id):
    url = f"{url_base}portal/company.aspx?id={id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def get_events(id, year):
    url = f"{url_base}api/events/page?companyId={id}&year={year}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type'):
        return response.json()
    return None

def extract_years_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    years_events = soup.find('input', {'id': 'EventsYears'})
    if years_events:
        return years_events.get('value').split(',')
    return []

def process_events(id):
    html = get_html(id)
    if not html:
        print(f"Error: Could not retrieve HTML for company {id}")
        return

    years = extract_years_from_html(html)
    if not years:
        print("No event years found.")
        return

    for year in years:
        events = get_events(id, year)
        if events:
            for event in events:
                print(f"Event: {event['eventName']} Date: {event['eventDate']}")
        else:
            print(f"No events found for year {year}")

# Main execution for specific ID range
for id in range(402, 403):  # Change range for more companies
    process_events(id)
