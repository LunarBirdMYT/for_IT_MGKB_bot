import threading
import time

from telebot import types

import config
import data.data_bot as db

easy_work = {
    'consultation': ('Консультация', 'Консультация успешно добавлена!'),
    'miac': ('Обращение в МИАЦ', 'Обращение в МИАЦ учтено!'),
    'egisz': ('Обращение в ЕГИСЗ', 'Обращение в ЕГИСЗ учтено!'),
    'frv_frk': ('Операции с ФРВ или ФРК', 'Действия с фед.регистрами учтены!'),
    'emias_pol': ('ЕМИАС Поликлиника', 'Действия с ЕМИАС Поликлиника учтены!'),
    'emias_stas': ('ЕМИАС Стационар', 'Действия с ЕМИАС Стационар учтены!')
    }
menu_install = {
    'install_crypto_pro': ('Установка КриптоПро', 'Установка крипты учтена!'),
    'install_true_conf': ('Установка TrueConf', 'Установка труконфа учтена!'),
    'install_ers_fss': ('Установка ЭРС от ФСС', 'Установка эрс учтена!'),
    'install_kasper': ('Установка Касперского', 'Установка каспера учтена!'),
    'install_any_po': ('Установка прочего ПО', 'Установка прочего ПО учтена!')
    }


def menu_func(button, user_id):
    buttons_menu = (
            button(text=easy_work['consultation'][0],
                   callback_data='consultation'),
            button(text=easy_work['miac'][0],
                   callback_data='miac'),
            button(text=easy_work['egisz'][0],
                   callback_data='egisz'),
            button(text='Установка ПО',
                   callback_data='install_po'),
            button(text=easy_work['frv_frk'][0],
                   callback_data='frv_frk'),
            button(text=easy_work['emias_pol'][0],
                   callback_data='emias_pol'),
            button(text=easy_work['emias_stas'][0],
                   callback_data='emias_stas'),
            button(text='Прочие активности',
                   callback_data='any_activity'),
            button(text='Как я там натрудился?🏥',
                   callback_data='my_activity'),
            button(text='Покажи мои прочие активности🏥',
                   callback_data='my_activity_another'),
            button(text='Вернуться в обычный режим🌏',
                   callback_data='back_normal_mode')
            )
    if user_id == config.USERS[2]:
        return buttons_menu + (
            button(text='Отчет за текущий месяц 🔥',
                   callback_data='report_now_month'),
            button(text='Отчет за предыдущий месяц 🔥',
                   callback_data='report_last_month'),
        )
    return buttons_menu


def activity_mode_func(bot):
    def create_record_db(message):
        """Создает запись о прочих работах в бд."""
        work = message.text
        if len(work) > 500:
            work = work[:500]
        user_id = message.from_user.id
        db.adding_any_work(user_id, work, config.USERS, is_any=True)
        kb_activity_res = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton
        for el in menu_func(button, user_id):
            kb_activity_res.add(el)
        bot.send_message(message.chat.id,
                         'Прочая активность учтена.',
                         reply_markup=kb_activity_res)

    @bot.message_handler(
        func=lambda message: message.text == 'Режим учёта активности')
    def activity_res(message):
        user_id = message.from_user.id
        kb_activity_res = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton
        for el in menu_func(button, user_id):
            kb_activity_res.add(el)
        bot.send_message(message.chat.id,
                         'Режим учета активности активирован!',
                         reply_markup=kb_activity_res)

    @bot.callback_query_handler(func=lambda callback: callback.data)
    def use_callback_data(callback):
        call = callback.message  # Вызов метода класса через эту переменную
        button = types.InlineKeyboardButton

        if callback.data in easy_work:
            user_id = callback.from_user.id
            db.adding_any_work(
                user_id,
                easy_work[callback.data][0],
                config.USERS
            )
            kb1 = types.InlineKeyboardMarkup(row_width=1)
            for el in menu_func(button, user_id):
                kb1.add(el)
            if call.text != easy_work[callback.data][1]:
                bot.edit_message_text(chat_id=call.chat.id,
                                      message_id=call.id,
                                      text=easy_work[callback.data][1],
                                      reply_markup=kb1)
            else:
                bot.edit_message_text(chat_id=call.chat.id,
                                      message_id=call.id,
                                      text=easy_work[callback.data][1] + '+1',
                                      reply_markup=kb1)

        elif callback.data == 'install_po':
            kb_install_po = types.InlineKeyboardMarkup(row_width=1)
            for key, value in menu_install.items():
                kb_install_po.add(
                    button(text=value[0],
                           callback_data=key)
                )
            bot.edit_message_text(chat_id=call.chat.id,
                                  message_id=call.id,
                                  text='Что ставили?',
                                  reply_markup=kb_install_po)
        elif callback.data in menu_install:
            user_id = callback.from_user.id
            db.adding_any_work(
                user_id,
                menu_install[callback.data][0],
                config.USERS
            )
            kb2 = types.InlineKeyboardMarkup(row_width=1)
            for el in menu_func(button, user_id):
                kb2.add(el)
            if call.text != menu_install[callback.data][1]:
                bot.edit_message_text(chat_id=call.chat.id,
                                      message_id=call.id,
                                      text=menu_install[callback.data][1],
                                      reply_markup=kb2)
            else:
                bot.edit_message_text(
                    chat_id=call.chat.id,
                    message_id=call.id,
                    text=menu_install[callback.data][1] + '+1',
                    reply_markup=kb2
                )
        elif callback.data == 'any_activity':
            user_id = callback.from_user.id
            send = bot.send_message(
                call.chat.id,
                'Отправьте сообщение о проделеннай работе.'
            )
            # Создаем поток
            thread_writer = threading.Thread(
                target=bot.register_next_step_handler,
                args=(send, create_record_db),
                daemon=True
            )
            # bot.register_next_step_handler(send, create_record_db)
            thread_writer.start()

        elif callback.data == 'my_activity':
            user_id = callback.from_user.id
            kb3 = types.InlineKeyboardMarkup(row_width=1)
            for el in menu_func(button, user_id):
                kb3.add(el)
            succesess_work = db.my_works(user_id)
            if not succesess_work:
                if call.text not in 'Записей нет.':
                    bot.edit_message_text(
                        chat_id=call.chat.id,
                        message_id=call.id,
                        text='Записей нет.',
                        reply_markup=kb3)
                    return
                else:
                    bot.edit_message_text(
                        chat_id=call.chat.id,
                        message_id=call.id,
                        text='Записей всё так же нет.',
                        reply_markup=kb3)
                    return
            text_work = ''
            for work, count in succesess_work:
                text_work += f'{work}: {count}\n'
            if call.text not in text_work:
                bot.edit_message_text(chat_id=call.chat.id,
                                      message_id=call.id,
                                      text=text_work,
                                      reply_markup=kb3)
            else:
                bot.edit_message_text(
                    chat_id=call.chat.id,
                    message_id=call.id,
                    text='Если ничего не делать, то ничего не изменится...',
                    reply_markup=kb3
                )
        elif callback.data == 'my_activity_another':
            user_id = callback.from_user.id
            kb4 = types.InlineKeyboardMarkup(row_width=1)
            for el in menu_func(button, user_id):
                kb4.add(el)
            succesess_work = db.my_another_works(user_id)
            if not succesess_work:
                if call.text not in 'Записей нет.':
                    bot.edit_message_text(
                        chat_id=call.chat.id,
                        message_id=call.id,
                        text='Записей нет.',
                        reply_markup=kb4)
                    return
                else:
                    bot.edit_message_text(
                        chat_id=call.chat.id,
                        message_id=call.id,
                        text='Записей всё так же нет.',
                        reply_markup=kb4)
                    return
            text_work = ''
            for number, work in enumerate(succesess_work, 1):
                text_work += f'{number}. {work}\n'
            if len(text_work) > 800:
                text_work = text_work[:800]
            if call.text not in text_work:
                bot.edit_message_text(chat_id=call.chat.id,
                                      message_id=call.id,
                                      text=text_work,
                                      reply_markup=kb4)
            else:
                bot.edit_message_text(
                    chat_id=call.chat.id,
                    message_id=call.id,
                    text='Что-то изменилось с последнего жмак по этой кнопке?',
                    reply_markup=kb4)
        elif callback.data == 'back_normal_mode':
            bot.delete_message(chat_id=call.chat.id,
                               message_id=call.id)
            kb_1 = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True)
            button = types.KeyboardButton
            kb_1.add(button(text='Linux🐧'),
                     button(text='Windows🪟'),
                     button(text='Веб ресурсы'))
            if callback.from_user.id == config.USERS[0]:
                kb_1.row(button(text='Режим учёта активности'))
            bot.send_message(call.chat.id,
                             'С чем работаем?',
                             reply_markup=kb_1)
        elif callback.data == 'report_now_month':
            user_id = callback.from_user.id
            kb5 = types.InlineKeyboardMarkup(row_width=1)
            for el in menu_func(button, user_id):
                kb5.add(el)
            # Раздел подсчитывамех работ
            succesess_work_count = db.all_works_now_month()
            text_work_count = ''
            for name, record, count in succesess_work_count:
                text_work_count += f'{name}: {record} - {count}\n'
            succesess_work = db.all_any_works_now_month()
            text_work = ''
            for name, record in succesess_work:
                text_work += f'{name}: {record}\n'

            if not succesess_work_count:
                bot.send_message(call.chat.id,
                                 'Странно, записей об обычных работах нет.')
            else:
                bot.send_message(call.chat.id,
                                 text_work_count)
            time.sleep(0.5)
            if not succesess_work:
                bot.send_message(call.chat.id,
                                 'Записей об индивидуальных работах нет.')
            else:
                bot.send_message(call.chat.id,
                                 text_work)
            time.sleep(0.5)
            bot.send_message(call.chat.id,
                             'Отчет предоставлен выше.',
                             reply_markup=kb5)
        elif callback.data == 'report_last_month':
            user_id = callback.from_user.id
            kb6 = types.InlineKeyboardMarkup(row_width=1)
            for el in menu_func(button, user_id):
                kb6.add(el)
            # Раздел подсчитывамех работ
            succesess_work_count = db.all_works_last_month()
            text_work_count = ''
            for name, record, count in succesess_work_count:
                text_work_count += f'{name}: {record} - {count}\n'
            succesess_work = db.all_any_works_last_month()
            text_work = ''
            for name, record in succesess_work:
                text_work += f'{name}: {record}\n'

            if not succesess_work_count:
                bot.send_message(call.chat.id,
                                 'Странно, записей об обычных работах нет.')
            else:
                bot.send_message(call.chat.id,
                                 text_work_count)
            time.sleep(0.5)
            if not succesess_work:
                bot.send_message(call.chat.id,
                                 'Записей об индивидуальных работах нет.')
            else:
                bot.send_message(call.chat.id,
                                 text_work)
            time.sleep(0.5)
            bot.send_message(call.chat.id,
                             'Отчет предоставлен выше.',
                             reply_markup=kb6)
