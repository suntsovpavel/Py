import random
import string

# Задача 0. Дан список, заполненный случайными числами от 0 до 10. 
#  Определите, является ли сумма всех элементов чётной.
# 1. 
# numbers = []
# for el in range(11):
#     numbers.append(el)

# 2. Если заранее известна длина
# len = 7
# numbers = [0] * len
# for index in range(len):
#     numbers[index] = 5

# 3. Случайные числа
# len = 7
# numbers = [0] * len
# for index in range(len):
#     numbers[index] = random.randint(0, 10)

# 4. Генератор
# numbers = [random.randint(0, 10) for i in range(len)]
# print(numbers)
# sum = 0
# for el in numbers:
#     sum += el
# # print(f'Сумма: {sum}')    
# if sum % 2 == 0:
#     print(f'Сумма {sum} четная')
# else:
#     print(f'Сумма {sum} нечетная')

# Задача 1. В списке хранятся сведения о количестве осадков, 
# выпавших за каждый день июня. Определите в какой период выпало больше осадков:
# в первой или второй половине июня.
# len = 30
# numbers = [random.randint(0, 10) for i in range(len)]
# print(numbers)
# sum, sum2 = 0, 0
# for index in range(15):
#     sum += numbers[index]
# for index in range(15, len):
#     sum2 += numbers[index]    
# if sum2 < sum:
#     print(f'Осадков больше выпало во второй половине: {sum} - {sum2}')    
# else:
#     print(f'Осадков больше выпало в первой половине: {sum} - {sum2}')    

# Задача 2. Напишите программу, которая позволит пользователю
# заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета
# dictionary = dict()
# dictionary['name'] = input('Введите имя: ')
# dictionary['age'] = int(input('Введите возраст: '))
# dictionary['hobby'] = input('Введите свое хобби: ')
# dictionary['animal'] = input('Введите свое любимое животное: ')
# print(f'Словарь: {dictionary}')

# !!! Добавить реализацию как на семинаре !!!!
# def Task2():
#     form = dict(Имя = input('Ваше имя: '), 
#                 Возраст = input('Ваш возраст: '), 
#                 Хобби = input('Ваше хобби: '), 
#                 Любимое_животное = input('Ваше любимое животное: '))
#     print()
#     for key, value in form.items():
#         print("{0}: {1}".format(key,value))
# Task2()

# Задача 3. Напишите скрипт генератора паролей
# заданной длины, состоящих из латинских букв и
# чисел.
# lenPassword = int(input('Введите длину пароля: '))
# source = string.ascii_letters + string.digits
# password = [source[random.randint(0, len(source)-1)] for _ in range(lenPassword)]
# # password = ''.join(random.sample(source, lenPassword))
# print(password)   

# Задача 4. Ручка стоит – 5 рублей, карандаш – 3
# рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу
# позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп».
# Определите сумму чека.
# dict = {'ручка':5, 'карандаш':3, 'ластик':4}
# sum = 0
# flag = True
# while flag:
#     code = input('Введите наименование: ').lower()
#     if code in dict.keys():
#         sum += dict[code]
#     elif code == 'стоп':
#         flag = False
# print(sum)

# for DZ:
data = open('sem3_test.txt', encoding='utf-8')
text = data.readlines()
phrase = text[0].split(':')
bot = {}
bot[phrase[0]] = phrase[1]
print(bot)

data.close()

q = input().lower()
print(bot[q])



