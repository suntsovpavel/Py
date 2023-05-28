# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot, time, json

bot = telebot.TeleBot("") 

# Конвертация message.date в читабельный вид
convertDate = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) 

@bot.message_handler(content_types=['text'])
def send_welcome(message):
 data = open('homework8/log.txt', mode='a', encoding='utf-8')
 saved_data = {'first_name':message.from_user.first_name,
               'last_name':message.from_user.last_name,
            'id':message.from_user.id,
            'date':convertDate(message.date),
            'message':message.text}
 data.write(json.dumps(saved_data) + '\n')
 data.close()    
 bot.reply_to(message, "Спасибо за оставленное сообщение. Вы получите ответ, как только наш сотрудник рассмотрит его")

bot.polling() 