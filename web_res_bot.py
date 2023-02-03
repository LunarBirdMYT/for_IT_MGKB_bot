import time
from telebot import types
import config


def web_res_func(bot):
    @bot.message_handler(func=lambda message: message.text == 'Веб ресурсы')
    def web_resources(message):
        kb_web_res = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               one_time_keyboard=True)
        button = types.KeyboardButton
        kb_web_res.row(button('Главное меню'),
                       button('Плагин для работы с ЕПГУ'))
        kb_web_res.row(button('Ссылки на веб ресурсы'),
                       button('Редирект на HTTPS'))
        kb_web_res.row(button('Пак сертификатов'),
                       button('Крипто плагин для Firefox'))
        bot.send_message(message.chat.id,
                         'Что Вас интересует?',
                         reply_markup=kb_web_res)
    
    
    @bot.message_handler(func=lambda message: message.text == 'Плагин для работы с ЕПГУ')
    def plagin_for_epgu(message):
        kb_plagin_epgu = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True)
        button = types.KeyboardButton
        kb_plagin_epgu.add(button('Главное меню'),
                           button('Веб ресурсы'))
        bot.send_message(message.chat.id,
                         'Вы можете скачать необходимый плагин по ссылке: https://ds-plugin.gosuslugi.ru/plugin/upload/Index.spr',
                         reply_markup=kb_plagin_epgu)
    
    
    @bot.message_handler(func=lambda message: message.text == 'Ссылки на веб ресурсы')
    def link_on_webpage(message):
        kb_on_webpage = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True)
        button = types.KeyboardButton
        kb_on_webpage.add(button('Главное меню'))
        bot.send_message(message.chat.id,
                         """
ГАСУ: https://gasu.mosreg.ru/index.php

ЕМИАС Поликлиника: http://main.emias.mosreg.ru/MIS/Mitishi_GKB/
ЕМИАС Поликлиника, шаблоны: https://template.softrust.ru/Admin/Account/Logon
ЕМИАС Стационар: http://hospital.emias.mosreg.ru/?c=portal

ЕЦУР: https://vk.ecur.mosreg.ru/login

ЕРИС ЛЛО 2022: http://llo.emias.mosreg.ru/mo2022

Мазки(рэдмайн): https://covid.rm.mosreg.ru/

Отчеты на BI: http://bi.mz.mosreg.ru/
Отчеты на reports: http://reports.emias.mosreg.ru/

Портал обучения от МИАЦ: https://edu.emias.mosreg.ru/

Почта мосрег: https://web.mail.mosreg.ru/SOGo/

ФР переболевших: https://covid.egisz.rosminzdrav.ru/
ФР вакцинированных: https://vaccine.egisz.rosminzdrav.ru
                         """,
                         reply_markup=kb_on_webpage)
    
    
    @bot.message_handler(func=lambda message: message.text == 'Редирект на HTTPS')
    def redirect_https(message):
        kb_redirect_https = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               one_time_keyboard=True)
        button = types.KeyboardButton
        kb_redirect_https.row(button('Главное меню'))
        bot.send_message(message.chat.id,
                         """
Действия, которые помогли с проблемой когда мозилла автоматом подставляет https.
Проверено на 4х компьютерах и пока все нормально работает.
Очищаем кеш/куки.
Далее идем в настройки - параметры сети выбираем Использовать системные настройки прокси
затем внизу в пункте Включить DNS через HTTPS вместо используемого провайдера Cloudflare добавил нового провайдера (в моем случае yandex.ru).
Нажимаем Ок
Заходим опять в параметры сети и снимаем галочку с пункта Включить DNS через HTTPS.
После этих манипуляций на HTTPS больше не редиректит.

На хроме в разделе "Безопасность", отключить безопасный DNS сервер, почти внизу. Потом очистить кеш и куки. Если не помогло:
На хроме можно в настройках прокси заредиректить на локальный сервер, типа 127.0.0.1, но тут нужно будет гуглить.
Так же:
Рекомендуем очистить SSL сертификаты в свойствах Интернет. Также проверьте, чтобы были включены все пункты TLS и SSL. Если производите работу в Chrome воспользуйтесь следующей рекомендацией:
Откройте страницу chrome://flags (введите этот адрес в адресную строку и нажмите Enter), выполните поиск (поле вверху страницы) по слову TLS и отключите параметр «Enforce deprecation of legacy TLS versions» (установите в Disabled), выполните то же самое для параметра «Experimental QUIC protocol». После этого нажмите по появившейся кнопке перезапуска браузера.
При любой из выбранных рекомендаций браузер необходимо перезагрузить.
Также после описанных действий проверьте открытие страницы в инкогнито. Настройки браузера вне инкогнито обновляются не сразу, поэтому необходимо удостовериться, что действия помогли именно через инкогнито.
                         """,
                         reply_markup=kb_redirect_https)
    
    
    @bot.message_handler(func=lambda message: message.text == 'Пак сертификатов')
    def send_sertificates(message):
        kb_send_sertificates = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               one_time_keyboard=True)
        button = types.KeyboardButton
        kb_send_sertificates.row(button('Главное меню'))
        bot.send_document(message.chat.id,
                          config.LINK_PACK_SERT_1)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_PACK_SERT_2)
        time.sleep(0.5)
        bot.send_message(message.chat.id,
                         'Для линукс. opt/itcs, и там файлик gui_bin')
        bot.send_document(message.chat.id,
                          config.LINK_PACK_SERT_3)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_PACK_SERT_4)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_PACK_SERT_5)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_PACK_SERT_6)
        time.sleep(0.5)
        bot.send_message(message.chat.id,
                         'isrgrootx1.der ставим как доверенные сертификаты. Инфа актуальна на 08.08.22',
                         reply_markup=kb_send_sertificates)


    @bot.message_handler(func=lambda message: message.text == 'Крипто плагин для Firefox')
    def plagin_for_firefox(message):
        kb_plagin_for_firefox = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                   one_time_keyboard=True)
        button = types.KeyboardButton
        kb_plagin_for_firefox.add(button('Главное меню'),
                           button('Веб ресурсы'))
        bot.send_message(message.chat.id,
                         'Вы можете добавить плагин по ссылке: https://www.cryptopro.ru/sites/default/files/products/cades/extensions/firefox_cryptopro_extension_latest.xpi',
                         reply_markup=kb_plagin_for_firefox)