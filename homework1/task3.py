# Задача 3. Напишите программу, которая по заданному
# номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))
if number == 1:
    print('Диапазон x, y: x > 0, y > 0')
elif number == 2:
    print('Диапазон x, y: x < 0, y > 0')
elif number == 3:
    print('Диапазон x, y: x < 0, y < 0')
elif number == 4:   
    print('Диапазон x, y: x > 0, y < 0')
else:
    print(f'Задан некорректный номер четверти: {number}')