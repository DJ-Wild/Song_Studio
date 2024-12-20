import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import requests
import sys
import traceback
import time

# Вставьте свой токен Telegram Bot API
API_TOKEN = '7141816414:AAHeoTdd6ZuDkqiYI702FN4_OKBsZ5KcnlA'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# URL вашего WebApp
WEB_APP_URL = "https://dj-wild.github.io/Song_Studio/"

# Ссылка на JSON с новостями
NEWS_URL = "https://dj-wild.github.io/Song_Studio/news.json"

news_cache = {}

# Словарь для хранения состояния пользователей
user_states = {}

# ID модератора (укажите правильный user_id)
MODERATOR_USER_ID = 1534688019  # Замените на правильный user_id

Exit = InlineKeyboardMarkup()
Exit.add(InlineKeyboardButton("Назад", callback_data="Exit"))

# Обработка всех ошибок
def log_error(exc_type, exc_value, exc_tb):
    """Глобальная обработка ошибок, вывод ошибок в консоль."""
    error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(f"Произошла ошибка: {error_message}")
    # Логируем ошибку в консоль
    bot.send_message(
        MODERATOR_USER_ID,  # Отправляем в личные сообщения модератору
        f"""Произошла ошибка: {error_message}""")

# Устанавливаем глобальный обработчик ошибок
sys.excepthook = log_error

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет сообщение с кнопкой для открытия Web App."""
    try:
        # Создание Web App кнопки
        web_app = WebAppInfo(url=WEB_APP_URL)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text="Открыть", web_app=web_app))

        bot.send_message(
            message.chat.id,
            "Привет! Это общедоступный бот DJ_Wild Song Studio! С помощью него вы можете почитать актуальные новости и график выхода песен! Для открытия страницы нажмите кнопку открыть. Чтобы узнать больше команд введите команду /help",
            reply_markup=markup
        )
    except Exception as e:
        print(f"Ошибка в send_welcome: {e}")

# Обработчик ошибок при подключении
def handle_infinity_polling():
    """Обработка ошибок во время infinity_polling с повторными попытками."""
    while True:
        try:
            # Основной цикл бота
            print("Бот запущен...")
            bot.infinity_polling(timeout=10, long_polling_timeout=10)  # Уменьшаем тайм-ауты
        except requests.exceptions.ConnectionError as e:
            print(f"Ошибка подключения: {e}. Повторная попытка через 5 секунд.")
            time.sleep(5)  # Задержка перед повтором
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            time.sleep(5)  # Задержка перед повтором

# Запуск с обработкой ошибок при подключении
if __name__ == "__main__":
    handle_infinity_polling()
    
