# 🌟 Horoscope Telegram Bot

Telegram-бот, который показывает ежедневный гороскоп для всех знаков зодиака.  
Данные берутся с реального сайта через парсинг.

---

## 🚀 Возможности

- Выбор знака зодиака через кнопки
- Получение актуального прогноза
- Парсинг данных с сайта horo.mail.ru
- Работа через Telegram Bot API (aiogram)

---

## 🧠 Как работает

1. Пользователь нажимает `/start`
2. Бот загружает список знаков зодиака
3. Показывает inline-кнопки
4. Пользователь выбирает знак
5. Бот парсит сайт и возвращает прогноз

---

## 🛠 Технологии

- Python 3
- aiogram
- requests
- BeautifulSoup (bs4)
- dotenv

---

## ⚙️ Установка


git clone https://github.com/USERNAME/horoscope-bot.git
cd horoscope-bot
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
