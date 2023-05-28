# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.

import telebot, json

bot = telebot.TeleBot("") 

# Читаем лог-файл и последовательно отвечаем на запросы пользователей
def reply():
 try:
  with open('homework8/log.txt', 'r', encoding='utf-8') as f:      
   lines = list(el for el in f.read().split('\n') if len(el)>0)
 except:
  print('Лог-файл не найден')

 for line in lines:
  data = json.loads(line)
  if 'id' in data and 'message' in data:
   bot.send_message(data['id'], f"Вы спрашивали {data['message']}")   
   bot.send_message(data['id'], f"Что-то отвечаем...")   
   # !!! Здесь надо либо чистить лог-файл, либо создавать лог ответов, 
   # чтобы не отвечать на запросы повторно. Пока этого нет

reply()