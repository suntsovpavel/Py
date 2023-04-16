import random

# Задача 0. Создайте кортеж. Запишите в него 10
# случайных чисел.

# numbers = tuple(random.randint(1,10) for _ in range(6))
# # numbers = [random.randint(1,10) for _ in range(6)]
# # numbers = tuple(numbers)

# print(numbers)
# print(type(numbers))

# Разыменование генератора:
# numbers = (random.randint(1,10) for _ in range(6))
# print(*numbers)

# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в
# кортеже по заданному индексу другим случайным числом.
# Решение 1. Преобразование в list и обратно
# def changeElement(tup, index, value):    
#     tup = list(tup)
#     tup[index] = value
#     tup = tuple(tup)
#     return tup
# # Решение 2. Использование срезов кортежей
# def changeElement(numbers, index):    
#     return numbers[:index] + (random.randint(1,10), ) + numbers[index+1:]

# tup = tuple(random.randint(1,10) for _ in range(6))
# print(tup)

# print(changeElement(tup, 4))


# На вход подаются два числа. Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел.
# def task2(x, y):
#     return (x+y, x-y, x*y, x/y)
# result = tuple(task2(3, 4))
# print(result)
# print(type(result))
# # распаковка кортежа:
# summa, razn, multiple, division = task2(3, 4)
# print(summa, razn, multiple, division)

# Задача 3:
# 15 мин
# Сгенерируйте список случайных чисел от 1 до 20,
# состоящий из 10 элементов. Удалите из списка
# дубликаты уже имеющихся элементов. Определите,
# сколько элементов было удалено.
# numbers =  [random.randint(1,10) for _ in range(10)]
# print(numbers)
# set_ = set(numbers)
# print(set_)
# print(f'Количество повторений: {len(numbers) - len(set_)}')

# Задача 4. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». 
# На главную роль нужен актёр обладающий всеми тремя качествами. 
# Определите, сколько есть претендентов на главную роль.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад

set1 = set('Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян'.split(' '))
set2 = set('Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад'.split(' '))
set3 = set('Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад'.split(' '))
print(set1.intersection(set2).intersection(set3))

