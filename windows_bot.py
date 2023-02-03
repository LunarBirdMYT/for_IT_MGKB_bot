import time
from telebot import types
import config


def windows_func(bot):
    @bot.message_handler(func=lambda message: message.text == 'Меню Windows🪟')
    @bot.message_handler(func=lambda message: message.text == 'Windows🪟')
    def windows_menu(message):
        kb_windows = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               one_time_keyboard=True)
        button = types.KeyboardButton
        kb_windows.row(button('Касперский🪟'),
                       button('Ассистент🪟'),
                       button('Библ.с++ для Ассистент🪟'))
        kb_windows.row(button('Сертификаты ЕГИСЗ и ЕПГУ🪟'),
                       button('КриптоПро 4.99🪟'))
        kb_windows.row(button('Проверка версии ЭРС от ФСС🪟'),
                       button('Главное меню'))
        bot.send_message(message.chat.id,
                         'Выберите желаемый продукт...',
                         reply_markup=kb_windows)

    @bot.message_handler(func=lambda message: message.text == 'Касперский🪟')
    def install_kasp(message):
        kb_kasp = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
        button = types.KeyboardButton
        kb_kasp.add(button('Меню Windows🪟'),
                    button('Главное меню'))
        bot.send_document(message.chat.id,
                          config.LINK_KASP,
                          reply_markup=kb_kasp)

    @bot.message_handler(func=lambda message: message.text == 'Ассистент🪟')
    def install_ass(message):
        kb_kasp = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
        button = types.KeyboardButton
        kb_kasp.add(button('Меню Windows🪟'),
                    button('Главное меню'))
        bot.send_message(message.chat.id,
                         config.ASSISTANT_SERVER)
        bot.send_document(message.chat.id,
                          config.LINK_ASS,
                          reply_markup=kb_kasp)

    @bot.message_handler(func=lambda message: message.text == 'Библ.с++ для Ассистент🪟')
    def install_ass_c(message):
        kb_install_ass_c = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                     one_time_keyboard=True)
        button = types.KeyboardButton
        kb_install_ass_c.add(button('Меню Windows🪟'),
                             button('Главное меню'))
        bot.send_document(message.chat.id,
                          config.LINK_ASS_C_1)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_ASS_C_2)
        time.sleep(0.5)
        bot.send_message(message.chat.id,
                         "Установить эти библиотеки в зависимости от бит, в крайнем случае переустановить ассистент.",
                         reply_markup=kb_install_ass_c)

    @bot.message_handler(func=lambda message: message.text == 'Сертификаты ЕГИСЗ и ЕПГУ🪟')
    def sert_egisz_and_epgu_for_windows(message):
        kb_sert = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
        button = types.KeyboardButton
        kb_sert.add(button('Windows🪟'),
                    button('Главное меню'))
        bot.send_message(message.chat.id,
                         'На всякий случай выкладываю сертификаты, которые нужно установить на АРМ с виндой, чтобы всё работало корректно. Оба корневых нужно установить в хранилище "Доверенные корневце центры сертификации", егисз и госуслуги можно устанавливать в хранилище по-умолчанию')
        time.sleep(1)
        bot.send_document(message.chat.id,
                          config.LINK_SERT_EGISZ_EGPU_1)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_SERT_EGISZ_EGPU_2)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_SERT_EGISZ_EGPU_3)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_SERT_EGISZ_EGPU_4,
                          reply_markup=kb_sert)

    @bot.message_handler(func=lambda message: message.text == 'КриптоПро 4.99🪟')
    def install_crypto_pro(message):
        kb_crypto_pro = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                  one_time_keyboard=True)
        button = types.KeyboardButton
        kb_crypto_pro.add(button('Меню Windows🪟'),
                          button('Главное меню'))
        bot.send_document(message.chat.id,
                          config.LINK_CRYPTO_4_99)
        time.sleep(0.5)
        bot.send_document(message.chat.id,
                          config.LINK_CRYPTO_4_99_txt,
                          reply_markup=kb_crypto_pro)

    @bot.message_handler(func=lambda message: message.text == 'Проверка версии ЭРС от ФСС🪟')
    def install_check_fss(message):
        kb_check_fss = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                 one_time_keyboard=True)
        button = types.KeyboardButton
        kb_check_fss.add(button('Меню Windows🪟'),
                         button('Главное меню'))
        bot.send_document(message.chat.id,
                          config.LINK_ERS_FSS_PROG)
        time.sleep(0.5)
        bot.send_message(message.chat.id,
                         '''
Прога написана на Python3. По сути это самораспаковывающийся архив, поэтому
Винда будет воспринимать его как вирус -> нужно разрешить исполнение.
В директории запуска появляется файл с датой версии, по умолчанию 06.04.2022(fss.version).
По кнопке "Проверить" обращается к сайту ФСС и проверяет дату последней версии на сайте,
после скачивания новой версии перезаписывая информацию о дате старой версии.
                        ''',
                         reply_markup=kb_check_fss)
