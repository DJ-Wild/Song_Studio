import telebot
from telebot.types import WebAppInfo, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import requests
import sys
import traceback

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
MODERATOR_USER_ID = 1534688019  # Замените на правильный user_id модератора

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

@bot.message_handler(commands=['help'])
def send_help(message):
    try:
        bot.send_message(message.chat.id, """
Команды:

/start - Выводит стартовое сообщение с переходом на страницу
/help - Выводит данное сообщение
/about - Выводит описание бота
/support - отправить сообщение модератору
/news - Показать последние новости
""", reply_markup=Exit)
    except Exception as e:
        print(f"Ошибка в send_help: {e}")

@bot.message_handler(commands=['about'])
def send_about(message):
    try:
        bot.send_message(message.chat.id, """
Это официальный бот DJ_Wild Song Studio(DJ_Wild SS)!

Вы можете посмотреть страницу студии(графики выхода песен и новости)

Также если появятся вопросы вы можете написать модерации по команде /support

Все команды можно узнать по команде /help

Дата создания: 17.12.24
Создатель: @xDJ_Wildx""", reply_markup=Exit)
    except Exception as e:
        print(f"Ошибка в send_about: {e}")

@bot.message_handler(commands=['news'])
def send_news(message):
    """Отправляет список новостей с кнопками для выбора."""
    try:
        # Загружаем данные из JSON-файла
        response = requests.get(NEWS_URL)
        response.raise_for_status()  # Проверяем, успешен ли запрос
        news_data = response.json()  # Парсим JSON

        if not news_data:
            bot.send_message(message.chat.id, "Новостей пока нет. Загляните позже!")
            return

        # Сохраняем новости в кэше (для упрощения доступа при обработке кнопок)
        news_cache[message.chat.id] = news_data

        # Создаем Inline-клавиатуру с кнопками
        markup = InlineKeyboardMarkup()
        for i, news in enumerate(news_data, start=1):
            title = news.get("title", "Без названия")
            button_text = f"{i}. {title}"
            markup.add(InlineKeyboardButton(button_text, callback_data=f"news_{i-1}"))
        markup.add(InlineKeyboardButton("Назад", callback_data="Exit"))
        # Отправляем клавиатуру пользователю
        bot.send_message(
            message.chat.id,
            "Выберите новость для чтения:",
            reply_markup=markup
        )
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки новостей: {e}")
        bot.send_message(message.chat.id, "Не удалось загрузить новости. Попробуйте позже.")
    except Exception as e:
        print(f"Ошибка в send_news: {e}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("news_"))
def handle_news_selection(call):
    """Обрабатывает выбор новости и выводит её содержимое."""
    try:
        # Получаем индекс новости из callback_data
        news_index = int(call.data.split("_")[1])

        # Проверяем, есть ли новости в кэше для пользователя
        user_news = news_cache.get(call.message.chat.id)
        if user_news is None or news_index >= len(user_news):
            bot.answer_callback_query(call.id, "Эта новость недоступна.")
            return

        # Получаем выбранную новость
        selected_news = user_news[news_index]
        title = selected_news.get("title", "Без названия")
        content = selected_news.get("content", "Нет содержания")

        # Отправляем новость пользователю
        bot.send_message(
            call.message.chat.id,
            f"📢 *{title}*\n\n{content}",
            parse_mode="Markdown", reply_markup=Exit
        )
        bot.answer_callback_query(call.id)  # Уведомляем Telegram, что запрос обработан
    except Exception as e:
        print(f"Ошибка в handle_news_selection: {e}")
        bot.answer_callback_query(call.id, "Произошла ошибка при загрузке новости.")

# Обработка команды /support
@bot.message_handler(commands=['support'])
def handle_support(message):
    """Отправляет сообщение с кнопками для подтверждения отправки жалобы."""
    try:
        # Создаем inline клавиатуру с кнопками "Да, уверен" и "Назад"
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("Да, уверен", callback_data="confirm_support"),
            InlineKeyboardButton("Назад", callback_data="cancel_support")
        )

        bot.send_message(
            message.chat.id,
            "Привет! Эта команда позволяет вам отправить сообщение модерации! Вы точно хотите написать модерации? Если сообщение будет ради веселья, то для вас доступ к боту ограничится!!!",
            reply_markup=markup
        )
    except Exception as e:
        print(f"Ошибка в handle_support: {e}")

# Обработка кнопок "Да, уверен" и "Назад"
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "confirm_support":
            # Сохраняем состояние пользователя для дальнейшей обработки
            user_states[call.message.chat.id] = 'awaiting_message'

            bot.send_message(
                call.message.chat.id,
                "Отлично! Пожалуйста, напишите сообщение о багах или проблемах, с которыми вы столкнулись."
            )
            bot.delete_message(call.message.chat.id, call.message.message_id)

        elif call.data == "cancel_support":
            bot.delete_message(call.message.chat.id, call.message.message_id)
        elif call.data == "Exit":
            bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as e:
        print(f"Ошибка в callback_query: {e}")

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: message.chat.id in user_states and user_states[message.chat.id] == 'awaiting_message')
def handle_user_message(message):
    try:
        # Сохраняем сообщение пользователя и его юзернейм
        user_states[message.chat.id] = 'message_sent'

        user_message = message.text
        username = message.from_user.username if message.from_user.username else "Неизвестно"

        # Отправляем сообщение модератору по user_id
        bot.send_message(
            MODERATOR_USER_ID,  # Отправляем в личные сообщения модератору
            f"""
#support
Пользователь: @{username}
Сообщение: {user_message}"""
        )

        # Отправляем подтверждение пользователю
        bot.send_message(
            message.chat.id,
            "Сообщение отправлено! Модератор может вам написать в ЛС!"
        )
    except Exception as e:
        print(f"Ошибка в handle_user_message: {e}")

# Обработка текстовых сообщений, если состояние не активировано
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        bot.reply_to(message, "Неопознанная функция🫠")
    except Exception as e:
        print(f"Ошибка в echo_all: {e}")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
