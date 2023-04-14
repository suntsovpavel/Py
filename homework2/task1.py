# Задача 1. Напишите программу, которая принимает на
# вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ]
# (1, 1*2, 1*2*3, 1*2*3*4)

def factirial(N: int):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

N = int(input('Введите число: '))
factorials = [factirial(i) for i in range(1, N+1)]
print(factorials)

