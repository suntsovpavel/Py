import numpy as np

# Задача 1. Проверьте, существует ли связь между
# данными, приведёнными в таблице.
# Выполните задание с помощью библиотеки numpy.
# [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
# [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
# [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]

def task1():
    nums_f = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    nums_s = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
    nums_t = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]
    
    matrix = [nums_f, nums_s, nums_t]
    
    result = np.corrcoef(matrix)
    print(result)


# Задача 2. Дан массив случайных чисел. Создайте
# его с помощью NumPy. Определите его среднее
# арифметическое.
# На ввод подаётся число. Определите ближайший по
# значению к нему элемент массива.
# [1.2, 4.2, 5.6, 7.1] -> 4.525
# 6.1 -> 5.6
def task2():    
    # !!! В python вместо массивов используются списки
    # Массив нам придется создать вручную
    size = 10
    numbers = np.random.randint(5, 15, size)
    print(numbers)
    
    # Сред.арифм
    mean = sum(numbers)/len(numbers)
    mean2 = np.mean(numbers)
    print(f'Сред.арифм. {mean}, {mean2}')
    
    # На ввод подаётся число. Определите ближайший по
    # значению к нему элемент массива.
    number = int(input('Введите число: '))
    # dist = list(map(lambda x: abs(x-number), numbers))
    dist = [abs(x-number) for x in numbers]
    print(f'дистанции: {dist}')
    min_dist = np.min(dist)
    print(f'мин. дистанция: {min_dist}')
    index_min_dist = dist.index(min_dist)
    print(f'индекс элемента с мин. дистанцией: {index_min_dist}')
    
#task2()

# Задача 3. Задайте квадратную матрицу, состоящую
# из случайных чисел. Найдите самый часто
# встречающийся элемент в этой матрице.
def task3():
    # Как бы эта задача решалась для одномерного массива:
    size = 10
    numbers = np.random.randint(1, 10, size)
    print(f'numbers: {numbers}')        
    numbers = list(numbers)
    print(f'numbers as list: {numbers}')  
    dict = {}
    for n in numbers:
        dict[n] = numbers.count(n)
    print('Ключи: числа, значения: сколько раз имеется в массиве:')        
    print(dict)        

    # Нужно получить список уникальных элементов (и их количество)    
    uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
    print(f'\nuniq_list = {uniq_list}')
    print(f'uniq_counts = {uniq_counts}')
    
    # Индекс элемента, встреченного в numbers макс.количество раз
    index_max = np.argmax(uniq_counts)
    print(f'Индекс элемента, встреченного в numbers макс.количество раз: {index_max}')
    print(f'Элемент {uniq_list[index_max]} встречается в numbers макс.количество раз: {uniq_counts[index_max]}')
    
    # Теперь все то же самое для двумерного массива
    size = (4,4)
    numbers = np.random.randint(1, 10, size)
    print(f'\nnumbers: {numbers}')    
    
    uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
    print(f'uniq_list = {uniq_list}')
    print(f'uniq_counts = {uniq_counts}')
    
    # Индекс элемента, встреченного в numbers макс.количество раз
    index_max = np.argmax(uniq_counts)
    print(f'Индекс элемента, встреченного в numbers макс.количество раз: {index_max}')
    print(f'Элемент {uniq_list[index_max]} встречается в numbers макс.количество раз: {uniq_counts[index_max]}')

#task3()

# Задача 4. Дан двумерный массив, заполненный
# нулями и единицами. Определите, есть ли в нём
# нулевые столбцы.
def task4():
    size = (3,10)
    numbers = np.random.randint(0, 2, size) # массив из 0 и 1
    print(f'numbers: {numbers}')        
    
    # Задавая axis 0 или 1, можно проверять столбцы / строки на наличие ненулевых значений:
    result = numbers.any(axis=0)
    print(result)
    result = ~result  # Применяем not к каждому элементу result
    print(result)
    if True in result:
        print(f'Матрица содержит столбец, состоящий только из нулей')  
    else:
        print(f'Матрица НЕ содержит столбцов, состоящих только из нулей')            
    
task4()    