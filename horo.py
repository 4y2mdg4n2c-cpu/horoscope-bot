import requests
import csv
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url_base = 'https://horo.mail.ru/'
url = url_base
def download_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print('Ошибка, время ожидания запроса истекло.')
        return None
    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')
        return None
    return BeautifulSoup(response.text, 'html.parser')
def get_signs():
    soup = download_page(url_base)
    if not soup:
        return None
    signs = []
    cards = soup.find_all('a', attrs={'data-qa': 'Link'})
    for card in cards:
        sign_tag = card.find('div', attrs={'data-qa': 'Text'})
        if not sign_tag:
            continue
        sign_name = sign_tag.text.strip()
        link = card.get('href')
        parent = card.find_parent()
        date_tag = None
        if parent:
            date_tag = parent.find('div', attrs={'data-qa': 'Text'})
        date = date_tag.text.strip() if date_tag else None
        signs.append({
            'знак': sign_name,
            'дата': date,
            'ссылка': link
        })

    return signs
def get_forecast(url):
    soup = download_page(url)
    if not soup:
        return None
    forecast = soup.find('div', attrs={'data-qa': 'ArticleItem'})
    if not forecast:
        return None
    return forecast.text.strip()
def get_horoscope_data():
    signs = get_signs()
    if not signs:
        return {}
    result = {}
    for sign in signs:
        full_url = urljoin(url_base, sign['ссылка'])
        forecast = get_forecast(full_url)
        if forecast:
            result[sign['знак'].lower()] = forecast
    return result