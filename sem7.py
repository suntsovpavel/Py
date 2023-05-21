import time
import telebot

def our_print():
    def other_print():
        print('123')
    other_print()
    
name_func = our_print  # поместили  функцию в переменную
name_func()
print(type(name_func))  # result: class 'function'

# 1. свой аналог функции filter
numbers = [2,45,1,4,2,6,878,3]
#print(list(filter(lambda x: x > 5, numbers)))

def our_filter(func, numbers):
    return (el for el in numbers if func(el))

print(list(our_filter(lambda x: x > 5, numbers)))

def compare_numbers(num):
    return num > 5    
print(list(our_filter(compare_numbers, numbers)))

# Задача 2. Создайте метод, позволяющий замерить время работы других методов.
def our_math_str():
    start_time = time.time()
    num = '123'
    result = int(num) + int(num*2) + int(num*3)
    print(f'время выполнения {time.time()-start_time}')

def our_math_int():
    start_time = time.time()
    num=123
    result = num + num*1000 + num*1000000 + num*1000 + num
    print(f'время выполнения {time.time()-start_time}')
our_math_str()
our_math_int()

def stopwatch(func):
    def decorator():
        start_time = time.time()
        func()
        print(f'время выполнения {time.time()-start_time}')
    return decorator       

@stopwatch
def our_math_str():
    num = '123'
    result = int(num) + int(num*2) + int(num*3)

# our_math_str()

#    other realisation stopwatch:
# --------------------------------
# def our_math_str():
#     num = '123'
#     result = int(num) + int(num*2) + int(num*3)
# stop = stopwatch(our_math_str)    
# stop()


# Задача 3. Создайте декоратор для метода нахождения суммы.
# а) функция sum не возвращает значение
def our_format(func):
    def decorator(*args):
        #print('Сумма чисел: ')            
        for arg in args:
            print(f'{arg} + ', end='')
        print('\b\b= ', end='')            
        func(*args)
    return decorator       

@our_format
def sum(a, b, c, d):
    print(a + b + c + d)
#sum(3,5,7,8)

# б) функция sum возвращает значение
def our_format(func):
    def decorator(*args):
        #print('Сумма чисел: ')            
        for arg in args:
            print(f'{arg} + ', end='')
        print('\b\b= ', end='')   
        result = func(*args)
        print(result)
        return result
    return decorator       

@our_format
def sum(a, b, c, d):
    return a + b + c + d
#print(sum(3,5,7,8))

# считаем числа фибоначчи рекурсией.
def stopwatch_fib(func):
    def decorator(N, count):
        if count==0:
            start_time = time.time()
        result = func(N, count)
        if count==0:
            print(f'время выполнения {time.time()-start_time}')       
        return result            
    return decorator  
@stopwatch_fib
def fib(N: int, count: int):
    return 1 if N<3 else fib(N-1, count+1) + fib(N-2, count+1)
print(f'fib(40) = {fib(40, 0)}')

# Задача 4. Создайте декоратор с параметрами.
# def greetings(hello):
#     def our_greetings(func):
#         def decorator():
#             name = func()
#             print(f'{hello}, {name}')
#         return decorator                
#     return our_greetings

# @greetings('Привет')
# def get_name():
#     return input('как тебя зовут?\n')
# get_name()



# Телеграм-бот
# https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py\

# import telebot
# import requests
# import time

# bot = telebot.TeleBot("6119292896:AAEZvqy8hW6fx42SKaWBr5_9qyI7NopYdaE") 

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(content_types=['text'])
# def greetings(message):
# 	text = message.text
# 	if text == 'котик':
# 		req = requests.get(f'https://cataas.com/cat?{time.time()}')
# 		bot.send_photo(message.from_user.id, req.content)
# 	# if 'привет' in text:
# 	#     bot.reply_to(message, f'Привет, {message.from_user.first_name}')
# 	# if text == 'погода':
# 	#     req = requests.get('https://wttr.in/?0T')
# 	#     bot.reply_to(message, req.text)

# bot.polling()