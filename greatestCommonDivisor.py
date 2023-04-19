
# !!! Известное правило:
# НОД(m, n) = НОД(n/m, n) при n>m, где n/m - деление целых

# реализовать алгоритм поиска наибольшего общего делителя двух целых m, n
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

print(greaterCommonDivisor(100, 35))