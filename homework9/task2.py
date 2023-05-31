# Задача 2. Создайте двумерный массив, размером 5х5. 
# Определите, есть ли в нём одинаковые строки.

import numpy as np

def task2():
    size = (5,5)
    numbers = np.random.randint(0, 2, size)
    print(f'numbers:\n', numbers)
    
    result = np.corrcoef(numbers)
    print(f'Таблица коэффициентов корреляции:\n {result}')
    
    # !!! Таблица коэффициентов корреляции может содержать nan
    # Тогда код работает некорректно !!!
    
    # получаем индексы всех единиц, встреченных в  result
    line_indexes, row_indexes = np.where(abs(result-1.)<1.e-7)
    print(f'Индексы строк единиц в result: {line_indexes}')
    print(f'Индексы столбцов единиц в result: {row_indexes}')
        
    # Если массив numbers содержит одинаковые строки,
    #  в result имеются единицы, стоящие не на главной диагонали
    # В этом случае массивы индексов line_indexes, row_indexes различаются    
    if np.array_equal(line_indexes, row_indexes):
        print(f'Массив numbers НЕ содержит одинаковых строк')
    else:
        print(f'Массив numbers содержит одинаковые строки')  

task2()