# Подключаем модуль для Телеграма
import os
import time
import telebot
from telebot import types
import config
from admin import admin_bot
from dotenv import load_dotenv
from linux_bot import linux_func
from windows_bot import windows_func
from web_res_bot import web_res_func
from activity_mode_bot import activity_mode_func


# Токен мгкб бота
load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)

# Админка бота
admin_bot(bot)


def tree_func():
    return ('Линукс\n'
            '---- Ассистент🐧\n'
            '-------- deb 🐧\n'
            '-------- rpm 🐧\n'
            '---- VipNet🐧\n'
            '-------- Установка VipNet🐧\n'
            '-------- Удаление VipNet🐧\n'
            '-------- Проблемы с VipNet🐧\n'
            '------------ sign Error🐧\n'
            '------------ Пароль к контейнеру🐧\n'
            '------------ Не удалось инициализировать криптопланины🐧\n'
            '---- Принтер HP 🐧\n'
            '---- Обновление Firefox 🐧\n'
            '---- Сменить пользователя 🐧\n'
            '---- Установка Chromium GOST 98 🐧\n'
            'Винда\n'
            '---- Касперский🪟\n'
            '---- Ассистент🪟\n'
            '---- Библ.с++ для Ассистент🪟\n'
            '---- Сертификаты ЕГИСЗ и ЕПГУ🪟\n'
            '---- КриптоПро 4.99🪟\n'
            '---- Проверка версии ЭРС от ФСС🪟\n'
            'Веб ресурсы\n'
            '---- Плагин для работы с ЕПГУ\n'
            '---- Ссылки на веб ресурсы\n'
            '---- Редирект на HTTPS\n'
            '---- Пак сертификатов\n'
            '---- Крипто плагин для Firefox\n'
            'Режим учёта активности')


# Начальная команда
@bot.message_handler(func=lambda message: message.text == 'Главное меню')
@bot.message_handler(commands=['start'])
def start(message):
    kb_1 = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True)
    button = types.KeyboardButton
    kb_1.add(button(text='Linux🐧'),
             button(text='Windows🪟'),
             button(text='Веб ресурсы'))
    kb_1.row(button(text='Покажи древо навыков'))
    if message.from_user.id in config.USERS:
        kb_1.row(button(text='Режим учёта активности'))
    bot.send_message(message.chat.id,
                     'С чем работаем?',
                     reply_markup=kb_1)


# По части линукси
linux_func(bot)

# По части винды
windows_func(bot)

# Веб ресурсы
web_res_func(bot)

# Режим активности
activity_mode_func(bot)


@bot.message_handler(commands=['help'])
def help_func(message):
    bot.send_message(message.chat.id,
                     """
Приветствую, коллега(если нет, то за Вами уже выехали 😈).

Данный бот призван облегчить работу сотрудникам ИТ Мытищинской ГКБ.
Запустите его при помощи команды /start.
Останавливать бота не нужно, рассылка какой-либо информации не планируется.
""")


@bot.message_handler(func=lambda message: message.text == 'Покажи древо навыков')
def skill_tree(message):
    kb_1 = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True)
    button = types.KeyboardButton
    kb_1.add(button(text='Linux🐧'),
             button(text='Windows🪟'),
             button(text='Веб ресурсы'))
    kb_1.row(button(text='Покажи древо навыков'))
    if message.from_user.id in config.USERS:
        kb_1.row(button(text='Режим учёта активности'))
    bot.send_message(message.chat.id,
                     tree_func(),
                     reply_markup=kb_1)

# Для добавления файлов


@bot.message_handler(func=lambda message: message.from_user.id == config.USERS[0],
                     content_types=['document', 'text', 'photo'])
def send_admin(message):
    bot.send_message(message.chat.id, message)


while True:
    try:
        print('Бот пашет за копейки...')
        bot.polling(none_stop=True)
        print('Бот уволился')
    except Exception as e:
        if "HTTPSConnectionPool" in str(e):
            time.sleep(5)
        with open(config.PATH_ERRORS, 'a+') as logs:
            print(f'Error:\n{str(e)}', file=logs)
        time.sleep(5)
