import telebot
import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

bot = telebot.TeleBot("") 

# Отвечаем на запросы пользователей
try:    
    connection = connect(
        host="localhost",        
        user='admin',                         
        password='',             
        database="temp_db");    
        
    # Вытаскиваем из messages_from_users запросы пользователей, на которые еще не даны ответы
    query = """SELECT messages_from_users.id,id_user,first_name,second_name,date,text FROM 
    messages_from_users INNER JOIN users ON id_primary_user = users.id
    WHERE id_user > 0 AND isAnswered = False"""    
    with connection.cursor() as cursor:            
        cursor.execute(query)             
        result = cursor.fetchall()   
        #print(result)                    
        
    while len(result)>0:         
        print(f' ---- \nСообщение от {result[0][2]} {result[0][3]} от {result[0][4]}:')  
        print(f'> {result[0][5]}')
        reply = input('Ответ пользователю:\n');
        
        # 1. Сохраняем ответ в answers
        query = """INSERT INTO answers (id_primary_messages,date,text) 
        VALUES (%s, NOW(), %s)"""
        with connection.cursor() as cursor:
            cursor.execute(query, (result[0][0], reply))
            connection.commit()     
            
        bot.send_message(result[0][1], f"На Ваш запрос '{result[0][5]}' отвечаем: {reply}")    
        
        # 2. Делаем отметку в messages_from_users, что ответ дан
        query = f"UPDATE messages_from_users SET isAnswered = True WHERE id = {result[0][0]}" 
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()                      
                                 
        result = result[1:]      
    print('Вуаля, работа закончена!')        
            
except Error as e:
    print('!!!except', e) 
