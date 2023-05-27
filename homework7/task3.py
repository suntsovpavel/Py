# Задача 3. Добавьте в telegram-бота игру «Угадай числа». 
# Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import random

bot = telebot.TeleBot("") 

isGame = False  # начата ли игра
number = 0
countTry = 0  # количество попыток

def initGame():
 global isGame, number, countTry
 countTry = 0
 number = random.randint(1,1000)    
 isGame = True 

@bot.message_handler(content_types=['text'])
def send_welcome(message):
 global isGame, number, countTry
 text = message.text.lower()
 if text == 'игра':
  if isGame:   
   bot.reply_to(message, "Игра уже запущена. Угадайте чиcло от 1 до 1000")
  else:
   bot.reply_to(message, "Угадайте чиcло от 1 до 1000")
   initGame() 
 elif text == 'стоп':  
  bot.reply_to(message, "Игра окончена")
  isGame = False  
 else:
  if isGame:
   if text.isdigit():
    countTry += 1
    userNumber = int(text)
    if userNumber == number:
     bot.reply_to(message, f'Поздравляем, Вы угадали число {number}! Количество попыток: {countTry}')
     isGame = False
    elif userNumber > number:
     bot.reply_to(message, f'Число {userNumber} больше загаданного')     
    elif userNumber < number:     
     bot.reply_to(message, f'Число {userNumber} меньше загаданного')
   else:
    bot.reply_to(message, 'Введенный Вами текст - не число')    
  else:
   bot.reply_to(message, "Чтобы начать игру, введите 'Игра'")    
     
bot.polling() 