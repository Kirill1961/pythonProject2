from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO Описание: Этот сайт был создан специально для обучения веб-скрейпингу и парсинга. На сайте представлены цитаты
#  известных людей, их авторы и теги. Пример парсинга: Вы можете извлекать цитаты, авторов и даты,
#  если они присутствуют на странице.
driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/")

# Извлекаем все цитаты
# quotes = driver.find_elements(By.CLASS_NAME, "text")
#
# for quote in quotes:
#     print(quote.text)
#
# driver.quit()


# TODO Описание: Сайт для учёбы, на котором представлены книги с ценами, рейтингами и описаниями.
#  Пример парсинга: Можно извлекать информацию о книгах, таких как название, цена и рейтинг.
driver.get("http://books.toscrape.com/")

# Извлекаем названия всех книг
# books = driver.find_elements(By.CLASS_NAME, "product_pod")
#
# for book in books:
#     title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
#     print(title)
#
# driver.quit()

# TODO . https://www.imdb.com/ (IMDb)
#  Описание: IMDb — это база данных фильмов,
#  актёров и т. д. Данные доступны для парсинга, хотя нужно учитывать,
#  что на сайте могут быть ограничения на автоматический сбор данных.
#  Пример парсинга: Вы можете извлечь список фильмов, их рейтинги и другие данные, такие как год выпуска.


# driver = webdriver.Chrome()
# driver.get("https://www.imdb.com/chart/top")
#
# # Извлекаем названия фильмов
# movies = driver.find_elements(By.CSS_SELECTOR, "td.titleColumn a")
#
# for movie in movies:
#     print(movie.text)
#
# driver.quit()

# TODO https://www.weather.com/
#  Описание:
#  На сайте можно извлечь информацию о погодных условиях для разных городов.
#  Пример парсинга: Извлечение текущей температуры, влажности и других метеоусловий для определённого города.


# driver = webdriver.Chrome()
# driver.get("https://weather.com/")
#
# # Извлекаем текущую температуру
# temperature = driver.find_element(By.CSS_SELECTOR, ".CurrentConditions--tempValue--MHmYY").text
# print(f"Current temperature: {temperature}")
#
# driver.quit()

#TODO https://www.nytimes.com/ (New York Times)
# Описание: На этом сайте можно извлекать статьи,
# заголовки новостей, а также информацию о времени публикации.
# Пример парсинга: Извлечение заголовков новостей и времени их публикации.
driver = webdriver.Chrome()
driver.get("https://www.nytimes.com/")

# Извлекаем заголовки новостей
headlines = driver.find_elements(By.CSS_SELECTOR, ".css-66vf3i a")

for headline in headlines:
    print(headline.text)

driver.quit()


