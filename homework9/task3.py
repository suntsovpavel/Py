# Задача 3. Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

def task3():
    num_lines = np.random.randint(2,7)
    print(f'num_lines = {num_lines}')
    num_rows = np.random.randint(2,7)
    print(f'num_rows = {num_rows}')    
    size = (num_lines, num_rows)
    numbers = np.random.randint(0, 101, size)
    print(f'numbers:\n', numbers)
    
    # Список уникальных элементов
    uniq_list = np.unique(numbers)
    print(f'Список уникальных элементов: {uniq_list}')

    # Поскольку uniq_list отсортирован по возрастанию,
    # минимальный и максимальный элементы находятся с начала и конца
    min_value = uniq_list[0] 
    max_value = uniq_list[-1] 
    
    # индексы минимальных элементов в numbers:
    line_indexes, row_indexes = np.where(numbers == min_value)
    # Выводим индексы первого встреченного [0] минимального элемента, если их несколько
    print(f'Индексы минимального элемента {min_value}: ({line_indexes[0]},{row_indexes[0]})')    

    # То же, максимальных
    line_indexes, row_indexes = np.where(numbers == max_value)
    print(f'Индексы максимального элемента {max_value}: ({line_indexes[0]},{row_indexes[0]})')                     
    
    # Получаем элементы главной диагонали
    # Если матрица не квадратная, считаем размер диагонали по наименьшему количеству строк и столбцов
    num_diagonal = min(num_lines, num_rows)
    
    # создаем пустой массив размера num_diagonal
    diagonal = np.zeros(num_diagonal)
    
    for i in range(num_diagonal):
        diagonal[i] = numbers[i][i]        
    print(f'Элементы главной диагонали: {diagonal}')                

task3()    