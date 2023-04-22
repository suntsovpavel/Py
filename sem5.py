# x = 10

import random

# def sum(x):
#     return x + 3

# # a = lambda x: x + 5
# # print(a)

# numbers = [1,2,3,5]

# # m = map(lambda x: x + 2, numbers)
# m = map(sum, numbers) 
# numbers = list(m)
# print(numbers)

# ff = filter(lambda x: x > 4, numbers)
# print(list(ff))


# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. 
# Заполните список случайным образом числами от 1 до 100.
def task0():
    numbers = [random.randint(0, 100) for i in range(15)]

    result = filter(lambda x: x % 5 == 0, numbers)

    print(list(result))

# Задача 1. На вход подаётся четырёхзначное число.
# Получите список, состоящий из цифр данного числа,
# увеличенных на 10.
# 20 мин
# 9650 –> [19, 16, 15, 10]
# 1043 –> [11, 10, 14, 13]

def task1():
    num= int(input('Введите число: '))
    digits = []
    while num > 0:
        digits.append((num % 10) + 10)
        num = num // 10
    digits.reverse()
    print(digits)

def task1_1():
    number = input("Enter number: ")
    number = [int(i) for i in number]
    result = list(map(lambda x: x % 10 + 10, number))
    print(result)

# Задача 2. В зоопарк отправили отчёт о новом поступлении
# зверей с ошибкой, в результате которой некоторые данные не
# расшифровались. Расшифруйте данные. Определите, в какой
# клетке находится лев. Номер клетки совпадает с номером
# строки.
# абвгдеёжзийклмнопрстуфхцчшщъыьэюя

# Преобразуем число в двоичное представление длиной 6 символов
def toBinary(num: int):
    result = ''
    while num > 0:
        result = str(num % 2) + result    
        num //= 2       
    return '0' * (6 - len(result)) + result    # Обеспечиваем вывод ровно 6 символов

# def decoder(code):
#     animal = [code[i:i+6] for i in range(0, len(code), 6)]
#     print(animal)


def task2():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    # !!! Каждая буква кодируется 6-ю символами, ибо 33 буквы, а 2**5 < 33 < 2**6
    animals = ['010100001100001001010011001011000000',
    '000001011100001011',
    '001011001111010011',
    '010010010011001111010001001111000111',
    '001100000101000010',
    '001011010001001111001100001001001011',
    '001101010100001100',
    '000001000000010001010010010100001011',
    '000011000101010000000000010001000100',
    '010010001111001101',
    '010010001111000001000000001011000000',
    '011000001001000111']

    alphabet = list(alphabet)
    d = {}
    for i in range(len(alphabet)):
        d[toBinary(i)] = alphabet[i]
    print(d)

    # Разбиваем кажду строку animals на элементы по 6 символов
    result = list(map(lambda x: [d[x[i:i+6]] for i in range(0, len(x), 6)], animals))
    print(result)
    result = list(map(lambda x: ''.join(x), result))
    print(result)

    # То же    
    animals_list = [''.join(alphabet[int(animal[x: x + 6], 2)] for x in range(0, len(animal), 6)) for animal in animals]
    print(animals_list)

task2()

