
# Задача 1. Дано натуральное число N. Напишите метод, 
# который вернёт список простых множителей числа N и количество этих множителей.

# Если число N - простое, возвращаем True, иначе False
def checkSimplyNumber(N: int):
    N=abs(N) # на случай, если передано отрицательное число
    i = 2
    while i < N:  # в промежутке (1,N) не должно встретиться делителей без остатка 
        if N % i == 0:
            return False
        i += 1
    return True

def getListSimplyNumericals(N: int):
    N=abs(N) # на случай, если передано отрицательное число
    
    numbers = []
    i = 2  # Первое из простых чисел
    fraction = N   # Результат последовательного деления N на множители, исходное присвоение
    while fraction > 1:
        if checkSimplyNumber(i):
            # Делим fraction на i, пока возможно деление без остатка 
            while (fraction % i == 0):
                fraction = fraction / i
                numbers.append(i)                        
        i += 1 
    return numbers       
    
N = int(input('Введите число: '))
print(f'Простые множители числа {N}: {getListSimplyNumericals(N)}')
        
