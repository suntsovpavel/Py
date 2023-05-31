import telebot
import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

bot = telebot.TeleBot("") 

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    # Проверяем, есть ли пользователь в таблице users и добавляем его, если его нет
    query = f"SELECT id FROM users WHERE id_user = {message.from_user.id}"      
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    if len(result) == 0:    # такого пользователя нет, добавляем
         query = """INSERT INTO users (id_user,first_name,second_name) VALUES (%s, %s, %s)"""                         
         with connection.cursor() as cursor:
             cursor.execute(query, 
                            (message.from_user.id, 
                             message.from_user.first_name, 
                             message.from_user.last_name))
             connection.commit() 

         query = "SELECT id FROM users ORDER BY id DESC LIMIT 1";      
         with connection.cursor() as cursor:
             cursor.execute(query)
             result = cursor.fetchall()                                
    id_users = result[0][0]          
    
    # Делаем запись сообщения пользователя в messages_from_users
    # Данное сообщение может быть продолжением беседы, 
    #   тогда нужно сохранить pointer_to на предыдущее сообщение. Пока присваиваеи NULL
    
    # !!! Здесь должна быть проверка того, что передал пользователь,
    # чтобы базу не сломать
    query = """INSERT INTO messages_from_users 
    (id_primary_user,date,text,isAnswered) VALUES (%s, NOW(), %s, False)"""   
    with connection.cursor() as cursor:
        cursor.execute(query, (id_users, message.text))
        connection.commit()     
            
    bot.reply_to(message, "Спасибо за оставленное сообщение. Вы получите ответ, как только наш сотрудник рассмотрит его")

try:
    connection = connect(
                host="localhost",
                user='admin',     
                password='',  
                database="temp_db");
    
    # query = "SHOW DATABASES";   # Запрос на получение списка баз данных
    # with connection.cursor() as cursor:
    #     cursor.execute(show_db_query)
    #     for db in cursor:
    #         print(db)    

    # Таблица уникальных пользователей
    query = """ CREATE TABLE IF NOT EXISTS users(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        id_user INT,
                        first_name VARCHAR(30),
                        second_name VARCHAR(30))"""                    
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()                    
              
    # Таблица запросов пользователей
    # id_primary_user = primary key from table users       
    query = """ CREATE TABLE IF NOT EXISTS messages_from_users(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        id_primary_user INT, 
                        date DATETIME, 
                        text TEXT,
                        isAnswered BOOLEAN)"""                
    with connection.cursor() as cursor:        
        cursor.execute(query)        
        connection.commit()    

    # Таблица ответов техподдержки
    # id_primary_messages =  primary key from messages_from_users
    query = """ CREATE TABLE IF NOT EXISTS answers(            
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_primary_messages INT,
        date DATETIME, 
        text TEXT)"""                
    with connection.cursor() as cursor:        
        cursor.execute(query)        
        connection.commit()        
        
    bot.polling() 
                    
except Error as e:
    print('!!!except', e)                    
