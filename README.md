# MGKB_bot
### Технологии:
![Telebot](https://img.shields.io/badge/Telebot-4.4.0-green)

### Описание:
Бот-справочник для нужд коллег. Пересылает ссылки на установщики программ, которые долго искать, некоторые команды, а так же скрипты на bash для Линукса. Реализованы кнопки посредством Reply. Для режима активности посредством Inline. Режим активности - отметки о выполненных работах с записью в БД SQLite. Сотрудник отнесенный к руководителю, просматривает статистику активности сотрудников с периодами "текущий месяц" и "предыдущий месяц."


### Как запустить проект:
Подразумевается, что ссылки на файлы, персонал с доступом и прочая необходимая информация для работы бота есть в config.py(по умолчанию файла в репозитории нет), помимо этого в файле .env данные токена.

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Запустить главный файл:
```
python main.py
```
