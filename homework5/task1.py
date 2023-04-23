import random

# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
def task1(N: int):
    N=abs(N)
    numbers = [random.randint(1,10) for _ in range(N)]    
    return (numbers, list(filter(lambda x: x > 5, numbers)))

N = int(input('Введите число: '))
numbers, result = task1(N)
print(f'numbers: {numbers}')
print(f'список элементов numbers, больших 5: {result}')
