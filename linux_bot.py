import time
from telebot import types
import config


def linux_func(bot):
    # По части линукси
    @bot.message_handler(func=lambda message: message.text == 'Linux🐧')
    def linux(message):
        kb_linux = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True)
        button = types.KeyboardButton
        kb_linux.add(button(text='Ассистент🐧'),
                     button(text='VipNet🐧'),
                     button(text='Принтер HP 🐧'),
                     button(text='Обновление Firefox 🐧'),
                     button(text='Сменить пользователя 🐧'),
                     button(text='Хромиум ГОСТ 98 🐧'))
        bot.send_message(message.chat.id,
                         'Выберите желаемый продукт...',
                         reply_markup=kb_linux)

    @bot.message_handler(func=lambda message: message.text == 'К выбору пакета ассистента')
    @bot.message_handler(func=lambda message: message.text == 'Ассистент🐧')
    def assistant_for_linux(message):
        kb_type_assistant = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                      one_time_keyboard=True)
        button = types.KeyboardButton
        kb_type_assistant.add(button(text='deb 🐧'),
                              button(text='rpm 🐧'))
        bot.send_message(message.chat.id,
                         'Какой пакет прислать?',
                         reply_markup=kb_type_assistant)

    @bot.message_handler(func=lambda message: message.text == 'deb 🐧')
    def assistant_deb(message):
        kb_type_assistant_deb = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                          one_time_keyboard=True)
        button = types.KeyboardButton
        kb_type_assistant_deb.add(button(text='К выбору пакета ассистента'),
                                  button(text='Главное меню'))
        bot.send_document(message.chat.id, config.LINK_DEB_ASS,
                          reply_markup=kb_type_assistant_deb)
        bot.send_message(message.chat.id,
                         'sudo apt-get install /путь до ассистента///'
                         f'{config.ASSISTANT_SERVER}')

    @bot.message_handler(func=lambda message: message.text == 'rpm 🐧')
    def assistant_rpm(message):
        kb_type_assistant_rpm = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                          one_time_keyboard=True)
        button = types.KeyboardButton
        kb_type_assistant_rpm.add(button(text='К выбору пакета ассистента'),
                                  button(text='Главное меню'))
        bot.send_document(message.chat.id, config.LINK_RPM_ASS,
                          reply_markup=kb_type_assistant_rpm)
        bot.send_message(message.chat.id,
                         'sudo apt-get install /путь до ассистента///'
                         f'{config.ASSISTANT_SERVER}')

    @bot.message_handler(func=lambda message: message.text == 'Меню VipNet🐧')
    @bot.message_handler(func=lambda message: message.text == 'VipNet🐧')
    def menu_vipnet(message):
        kb_menu_vipnet = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True,
                                                   row_width=2)
        button = types.KeyboardButton
        kb_menu_vipnet.add(button(text='Установка VipNet🐧'),
                           button(text='Удаление VipNet🐧'),
                           button(text='Проблемы с VipNet🐧'),
                           button(text='Главное меню'))
        bot.send_message(message.chat.id,
                         'Какой вариант Вам подойдёт сегодня?',
                         reply_markup=kb_menu_vipnet)

    @bot.message_handler(func=lambda message: message.text == 'Установка VipNet🐧')
    def install_vipnet(message):
        kb_vipnet_install = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                      one_time_keyboard=True)
        button = types.KeyboardButton
        kb_vipnet_install.add(button(text='Меню VipNet🐧'),
                              button(text='Главное меню'))
        bot.send_message(message.chat.id,
                         """
Вы можете запустить приложенный файл на рабочем месте и установить Vipnet,
а можете следовать инструкции по самостоятельной установке:
cd /opt/vipnet_pki_16_update
ls
sudo sh /opt/vipnet_pki_16_update/install.sh

Поздравляю, Вы со всем, возможно, успешно справились!
                         """)
        bot.send_document(message.chat.id,
                          config.LINK_INSTALL_VIPNET,
                          reply_markup=kb_vipnet_install)

    @bot.message_handler(func=lambda message: message.text == 'Удаление VipNet🐧')
    def delete_vipnet(message):
        kb_delete_vipnet = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                     one_time_keyboard=True)
        button = types.KeyboardButton
        kb_delete_vipnet.add(button(text='Меню VipNet🐧'),
                             button(text='Главное меню'))
        bot.send_message(message.chat.id,
                         """
Вы можете запустить приложенный файл на рабочем месте и удалить Vipnet,
а можете следовать инструкции по самостоятельному удалению:
Копируем лицензию на всякий случай в домашний каталог
cp /opt/itcs/share/pki-client/license/1.itcslic ~/1.itcslic

sudo apt-get remove 'itcs-*'

Следует убедиться, что все файлы были удалены(если ноль, то файлов нет):
ls -l /opt/itcs/ | grep ".prg\|.CRG" | wc -l

Если все файлы удалены, то перезагружаемся, если нет, то Вам нужна помощь.
                         """)
        bot.send_document(message.chat.id,
                          config.LINK_DELETE_VIPNET,
                          reply_markup=kb_delete_vipnet)

    @bot.message_handler(func=lambda message: message.text == 'Меню проблем с Vipnet🐧')
    @bot.message_handler(func=lambda message: message.text == 'Проблемы с VipNet🐧')
    def vipnet_gudes(message):
        kb_troubles_vipnet = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                       one_time_keyboard=True)
        button = types.KeyboardButton
        kb_troubles_vipnet.add(button(text='sign Error🐧'),
                               button(text='Пароль к контейнеру🐧'),
                               button(
                                   text='Не удалось инициализировать криптопланины🐧'),
                               button(text='Главное меню'))
        bot.send_message(message.chat.id, 'Укажите проблему...',
                         reply_markup=kb_troubles_vipnet)

    # Функция для возвращения к ошибкам с випнет

    def vipnet_gudes_return(message):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True)
        button = types.KeyboardButton
        kb.add(button(text='Меню проблем с Vipnet🐧'),
               button(text='Главное меню'))
        return kb

    # Проблемы при работе с випнет

    @bot.message_handler(func=lambda message: message.text == 'sign Error🐧')
    def sign_error(message):
        kb_for_troubles = vipnet_gudes_return(message)
        bot.send_message(message.chat.id,
                         """
Рекомендации от Алексея Долгих:
По ошибке sign error:
Переустановить vipnet pki, но лучше:
Обязательно проверьте, что лицензия для ViPNet CSP установлена командой:
/opt/itcs/bin/license status --product=csp_linux
В выводе должен присутствовать статус State: Valid
Если нет valid:
/opt/itcs/bin/pki-client-license --csp /opt/itcs/share/pki-client/license/1.itcslic
Перезагрузиться

Проверьте, работает ли ЭЦП со вставленным токеном врача(только открытая часть).
                         """)
        bot.send_document(message.chat.id,
                          config.LINK_SING_ERROR,
                          reply_markup=kb_for_troubles)

    @bot.message_handler(func=lambda message: message.text == 'Пароль к контейнеру🐧')
    def password_on_vipnet(message):
        kb_for_troubles = vipnet_gudes_return(message)
        bot.send_photo(message.chat.id,
                       config.LINK_IMG_PASS_CONT_1)
        bot.send_message(message.chat.id,
                         """
Из-за того что контейнер имеет в названии пробел, скобки и кириллицу на
линукс не может переместиться закрытая часть контейнера.
                         """)
        time.sleep(1)

        bot.send_photo(message.chat.id,
                       config.LINK_IMG_PASS_CONT_2)
        bot.send_message(message.chat.id,
                         """
На АРМ под windows запустить ViPNet CSP выбрать контейнер для копирования
и нажать на "Копировать в" После откроется окно "инициализация контейнера
ключей". В поле Имя контейнера можно сменить имя.
Скобки и знаки препинания не использовать
    
                         """)
        bot.send_photo(message.chat.id,
                       config.LINK_IMG_PASS_CONT_3,
                       reply_markup=kb_for_troubles)

    @bot.message_handler(func=lambda message: message.text == 'Не удалось инициализировать криптопланины🐧')
    def linux_cryptoplag(message):
        kb_linux_crypto = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                    one_time_keyboard=True)
        button = types.KeyboardButton
        kb_linux_crypto.add(button(text='Главное меню'),
                            button(text='Linux🐧'))
        bot.send_message(message.chat.id,
                         """
Стандартно это решается удалением винпнета, переустановкой, 
что занимает много времени в целом. Но сегодня нашел другой способ: 
1) Можно попробовать выйти из випнета(меню в панели задач), и запустить випнет веб.
Выбрать сертификаты по умолчанию. Врач сможет подписывать ЭЛН, единственное, 
что ему нужно будет при подписи вводить пароль. 
Но как плюс мы не тратим время на переустановку, звонок врачу, 
который должен будет войти в систему, потом установку, 
звонок врачу для перезагрузки и снова входа в систему.
2) Если не помогло, то cd/opt/vipnet_pki_15, заходим в каталог
и вводим команду в консоле sudo sh /opt/vipnet_pki_15/install.sh
потом пункт 1. 

Это как вариант решить вопрос быстро, а потом уже по наличию времени можно и с переустановкой, потому что неизвестно что будет у врача завтра после перезагрузки.
                         """,
                         reply_markup=kb_linux_crypto)

    @bot.message_handler(func=lambda message: message.text == 'Принтер HP 🐧')
    def install_hp(message):
        kb_install_hp = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                  one_time_keyboard=True)
        button = types.KeyboardButton
        kb_install_hp.add(button(text='Главное меню'))
        bot.send_message(message.chat.id,
                         """
Вы можете запустить приложенный файл на рабочем месте и установить принтер HP,
а можете следовать инструкции по самостоятельной установке:
Обновляем apt-кеш и устанавливаем пакеты:

sudo apt-get update
sudo apt-get install hplip hplip-gui hplip-recommends hplip-gui-autostart
sudo salt-call state.apply
перезагрузка арма
sudo hp-setup –i
sudo hp-plugin

Далее отвечаем на вопросы при установке.
                         """)
        bot.send_document(message.chat.id,
                          config.LINK_INSTALL_HP,
                          reply_markup=kb_install_hp)

    @bot.message_handler(func=lambda message: message.text == 'Обновление Firefox 🐧')
    def update_firefox(message):
        kb_update_firefox = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                      one_time_keyboard=True)
        button = types.KeyboardButton
        kb_update_firefox.add(button(text='Главное меню'),
                              button(text='Linux🐧'))
        bot.send_message(message.chat.id,
                         """
В две команды:
sudo apt-get update
sudo apt-get install firefox-esr firefox-esr-ru

                         """,
                         reply_markup=kb_update_firefox)

    @bot.message_handler(func=lambda message: message.text == 'Сменить пользователя 🐧')
    def change_user(message):
        kb_change_user = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True)
        button = types.KeyboardButton
        kb_change_user.add(button(text='Главное меню'),
                           button(text='Linux🐧'))
        bot.send_message(message.chat.id,
                         """
На Альтах (Fedora) меняется так:
"su - логин_пользователя"
Обратите внимание на пробелы - они обязательны.

                         """,
                         reply_markup=kb_change_user)

    @bot.message_handler(func=lambda message: message.text == 'Хромиум ГОСТ 98 🐧')
    def install_chr_gst(message):
        kb_install_chr_gst = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                       one_time_keyboard=True)
        button = types.KeyboardButton
        kb_install_chr_gst.add(button(text='Главное меню'),
                               button(text='Linux🐧'))
        bot.send_message(message.chat.id,
                         """
Устанавливаем пакет:

sudo apt-get install chromium-gost-stable-98.0.4758.102-alt1.repacked.with.epm.2.x86_64.rpm

Можно добавить в избранное и на рабочий стол.
                         """)
        bot.send_document(message.chat.id,
                          config.LINK_CHROMIUM_GS,
                          reply_markup=kb_install_chr_gst)
