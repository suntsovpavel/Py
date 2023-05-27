# Задача 3. Добавьте в telegram-бота игру «Угадай числа». 
# Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import random

bot = telebot.TeleBot("") 

isGameStarted = False  # начата ли игра
number = 0    # загаданное число
countTry = 0  # количество попыток

def initGame():
 global isGameStarted, number, countTry
 countTry = 0
 number = random.randint(1,1000)    
 isGameStarted = True 

@bot.message_handler(content_types=['text'])
def send_welcome(message):
 global isGameStarted, number, countTry
 text = message.text.lower()
 if text == 'игра':
  if isGameStarted:   
   bot.reply_to(message, "Игра уже запущена. Угадайте чиcло от 1 до 1000")
  else:
   bot.reply_to(message, "Угадайте чиcло от 1 до 1000")
   initGame() 
 elif text == 'стоп':  
  bot.reply_to(message, "Игра окончена")
  isGameStarted = False  
 else:
  if isGameStarted:
   if text.isdigit():
    countTry += 1
    userNumber = int(text)
    if userNumber == number:
     bot.reply_to(message, f'Поздравляем, Вы угадали число {number}! Количество попыток: {countTry}')
     isGameStarted = False
    elif userNumber > number:
     bot.reply_to(message, f'Число {userNumber} больше загаданного')     
    elif userNumber < number:     
     bot.reply_to(message, f'Число {userNumber} меньше загаданного')
   else:
    bot.reply_to(message, 'Введенный Вами текст - не число')    
  else:
   bot.reply_to(message, "Чтобы начать игру, введите 'Игра'")    
     
bot.polling() 