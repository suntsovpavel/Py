import random

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

# Случайным образом выбираем элементы из numbers 
#   до тех пор, пока последовательность значений возрастает
def getIncreasingSeries(numbers: list):  
    # вспомогательный список индексов массива numbers:
    indexes = [i for i in range(len(numbers))]      

    result = [] 
    while len(indexes) > 0:  
        index = indexes.pop(random.randint(0, len(indexes)-1))             

        if len(result) == 0 or numbers[index] > result[-1]:
            result.append(numbers[index])
        else:
            return result    

def task2():
    # cоздаем список, заполненный случайными числами от 1 до 10
    N = abs(int(input('Введите число: ')))
    numbers = [random.randint(1,10) for _ in range(N)]   
    print(f'numbers: {numbers}')

    # Повторяем попытки до тех пор, пока не будет получена последовательность более чем из одного элемента
    flag = True
    while flag:
        result = getIncreasingSeries(numbers)
        if len(result) > 1:
            print(result)
            flag = False
task2()

    
    


