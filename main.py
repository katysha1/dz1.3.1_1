# https://ru.wikipedia.org/wiki/Python
# Реализовать парсер, который собирает все заголовки 3 уровня(h3), со страницы https://ru.wikipedia.org/wiki/Python и сохраняет их в текстовый файл
import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Python'
# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    print("Запрос выполнен успешно!")
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    h3_tags = soup.find_all('h3')
    for tag in h3_tags:
        print(tag.get_text())

    with open("response.text", "w") as file:
        file.write("Заголовки 3 уровня")

    print("Содержимое страницы:", response.text[:200])  # Выводим первые 200 символов
else:
    print("Произошла ошибка:", response.status_code)





