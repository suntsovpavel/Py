
# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def Fibonacci(N: int):
    return 1 if (N<3) else (Fibonacci(N-1) + Fibonacci(N-2))

def task1(namefile, N: int):    
    numbers = [Fibonacci(i) for i in range(1,N+1)]
    with open(namefile, 'w', encoding='utf-8') as f:
        f.write(str(numbers))
    return numbers        
 
N = int(input('Введите число: '))
namefile = input('Введите имя файла(без расширения): ')
namefile += '.txt'

numbers = task1('homework3/' + namefile, N)
print(f'numbers Fibonacci: {numbers}')
print(f'file {namefile} is created')