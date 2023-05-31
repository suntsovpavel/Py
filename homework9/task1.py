# Задача 1. Дан список элементов. Используя библиотеку NumPy, 
# подсчитайте количество уникальных элементов в нём.

import numpy as np

def task1():
    size = int(input('Введите размер массива: '))
    numbers = np.random.randint(1, 10, size) 
    
    # ПРеобразуем в список, согласно заданию
    numbers = list(numbers)
    print(f'numbers: {numbers}')
    
    uniq_list = np.unique(numbers)
    print(f'Список уникальных элементов в numbers: {uniq_list}')    
    print(f'Количество уникальных элементов: {uniq_list.size}')
    
task1()