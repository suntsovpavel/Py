# Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.

# алгоритм поиска наибольшего общего делителя двух целых m, n
def greaterCommonDivisor(m: int, n: int):
    # 1. Базовый алгоритм
    # if m == n:
    #     return m
    # result = 1
    # for i in range(2, min(m, n)+1):
    #     if m % i == 0 and n % i == 0:
    #         result = i
    # return result                
    
    # 2. Продвинутый алгоритм
    while m > 0:
        tmp = n % m
        n = m
        m = tmp
    return n      

def task3():
    result = []    
    # Перебираем знаменатели:
    for i in range(2,12):
        # Перебираем числители от 1 до i, т.к. дроби менее 1
        for j in range(1, i):
            # признак несократимой дроби: НОД = 1
            if greaterCommonDivisor(i, j) == 1:   
                result.append(str(j) + '/' + str(i))
    return result                

print(task3())