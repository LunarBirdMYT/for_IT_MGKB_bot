import config


def admin_bot(bot):
    # Если пользователя нет в спсике, то бот не активен
    @bot.message_handler(
        func=lambda message: message.from_user.id not in config.USERS,
        content_types=['document', 'text', 'photo', 'sticker'])
    def if_not_partner(message):
        # Добавляем обращенца в файл с пользователями
        new_user_id = message.from_user.id
        name = message.from_user.first_name
        surname = message.from_user.last_name
        username = message.from_user.username
        user_in_bd = f'{new_user_id}-R-_{name}-R-_{surname}-R-_{username}'

        with open(config.PATH_BAN_USERS,
                  'r',
                  encoding='utf-8-sig') as users_db:
            list_users = [stri.strip() for stri in users_db.readlines()]
            if user_in_bd not in list_users:
                with open(config.PATH_BAN_USERS,
                          'a+',
                          encoding='utf-8-sig') as users_db:
                    print(user_in_bd, file=users_db)
                    bot.send_message(
                        config.USERS[0],
                        f'У нас тут новый изверь\n{user_in_bd}'
                    )
        del new_user_id, name, surname, username, user_in_bd
        # Если пользователь не сотрудник, то уведомляем его
        bot.send_message(message.chat.id,
                         'Вы не являетесь сотрудником МГКБ.'
                         'Доступ ограничен!Свяжитесь с руководителем ОВСиПИС'
                         'для получения доступа.')

    # Добавляем в черный список пользователя
    @bot.message_handler(
        func=lambda message: message.from_user.id == config.USERS[0]
        and 'Добавь' in message.text)
    def add_black_list(message):
        add_user_list = int(message.text.split()[1])
        config.USERS.append(add_user_list)
        bot.send_message(message.chat.id,
                         f'Человек с id {add_user_list} добавлен в USERS')
