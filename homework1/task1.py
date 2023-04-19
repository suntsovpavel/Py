# Задача 1. Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели.

number = int(input('Введите цифру, обозначающую день недели:\n'))
days = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
if number > 0 and number < 8:
    print(days[number-1])   # номера дней от единицы, а индексация от нуля
else:
    print('Нет такого дня')

