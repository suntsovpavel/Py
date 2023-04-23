import math

# Задача 3. Выведите число PI с заданной точностью. Точность выводится в виде десятичной дроби.

# возвращаем цифру числа на позиции N дробной части 
# например, для value=1.234567 для N=1 return 2, для N=2 return 3 и т.д.    
def getDigit(value: float, N: int):
    return int(value * 10**N) % 10
        
def task3(eps: float, maxDigits: int = 100):
    pi_result = '3.'    
    # перемещаем позицию дробной части и добавляем знаки в result,
    #   пока в eps не встретится цифра, отличная от нуля:  
    for i in range(1,maxDigits+1):
        pi_result += str(getDigit(math.pi, i))
        if getDigit(eps, i) != 0: 
            break            
    return pi_result            

eps = float(input('Введите точность eps: '))
print(f'Число pi с точностью {eps}: {task3(eps)}')

# def task3(eps: float):
#     return math.pi - math.pi % eps;    
