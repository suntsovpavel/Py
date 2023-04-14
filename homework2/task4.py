# Задача 4. Задайте список из N элементов, заполненных
# числами из промежутка [-N, N]. Сдвиньте все элементы
# списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

# вгоняем смещенный индекс элемента списка в допустимый диапазон (-len, len)
def shiftIndex(index, len):
    if len > 0:      # иначе получим бесконечный цикл
        while index >= len:
            index -= len
        while index <= -len:
            index += len    
    return index

def formNumbers(N: int):
    N = abs(N)   # на случай, если будет задано N<0
    return [i for i in range (-N,N+1)] 

N = int(input('Введите число: '))
numbers = formNumbers(N)
print(f'Исходный список: {numbers}')

shift = -2      # = int(input('Введите смещение: '))
len = len(numbers)
numbers2 = [numbers[shiftIndex(i + shift, len)] for i in range(len)]
print(f'Список со смещением элементов: {numbers2}')