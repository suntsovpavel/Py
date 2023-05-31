
* Устанавливаем [MySQL Server](https://dev.mysql.com/downloads/installer/) (localhost)

* Создаем БД temp_db и пользователя admin. Находим в task1.py,task2.py строки password='' и вписываем внутрь кавычек админский пароль

* pip install mysql-connector-python

* pip install MySQL

* pip install pyTelegramBotAPI. Создаем бота (см. семинар 7), ищем в task1.py,task2.py строки bot = telebot.TeleBot("") и вписываем внутрь кавычек ключ бота 

* Запускаем сначала task1.py и пишем боту сообщения. Останавливаем task1.py, запускаем task2.py и пишем ответы пользователю. Если предыдущие шаги сделаны правильно, всё должно быть ок

[в помощь](https://proglib.io/p/python-i-mysql-prakticheskoe-vvedenie-2021-01-06)