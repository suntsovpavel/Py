
import random

# Задача 1. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.
# def task1(n: int):
#     N = [random.randint(0, 10) for _ in range(n)]    
#     print(f'n: {N}')
#     setN = set(N)
#     print(f'set: {setN}')
#     if len(setN) != len(N):
#         print(f'элементы списка НЕ уникальны')
#     else:
#         print(f'все элементы списка не уникальны')    
# task1(10)         

# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.
# def task2(n: int, n2: int):
#     str_n = str(n)
#     set1 = set([int(i) for i in str_n])
#     print(f'set1: {set1}')

#     str_n2 = str(n2)
#     set2 = set([int(i) for i in str_n2])
#     print(f'set2: {set2}')

#     if set1 == set2:
#         print('числа состоят из одних и тех же цифр')
#     else:
#         print('числа состоят НЕ из одних и тех же цифр') 

# 2. С учетом количества цифр:
# def task2(n: int, n2: int):
#     str_n = str(n)
#     list1 = [int(i) for i in str_n]
#     list1.sort();
#     print(f'list1: {list1}')
    
#     str_n2 = str(n2)
#     list2 = [int(i) for i in str_n2]
#     list2.sort();
#     print(f'list2: {list2}')

#     if list1 == list2:
#         print('числа состоят из одних и тех же цифр')
#     else:
#         print('числа состоят НЕ из одних и тех же цифр') 

# task2(22345, 54422)

# Alternative:
# def same_digits(num1, num2):
#     digits = [0] * 10

#     while num1 > 0:
#         digit = num1 % 10
#         digits[digit] += 1
#         num1 //= 10

#     while num2 > 0:
#         digit = num2 % 10
#         digits[digit] -= 1
#         num2 //= 10

#     for count in digits:
#         if count != 0:
#             return False

#     return True        

# print(same_digits(22345, 51422))

# Решение преподавателя
# def task2(number_f: int, number_s: int):
#     # согставляем словарь 'цифра':'сколько раз встречается в числе'

#     num_f_dict = dict((i, str(number_f).count(i)) for i in set(str(number_f)))
#     print(f'num_f_dict = {num_f_dict}')

#     num_s_dict = dict((i, str(number_s).count(i)) for i in set(str(number_s)))
#     print(f'num_s_dict = {num_s_dict}')

#     if num_f_dict == num_s_dict:
#         print('числа состоят из одних и тех же цифр')
#     else:
#         print('числа состоят НЕ из одних и тех же цифр') 

# task2(22345, 54322)   


# Задача 3. Напишите программу вычисления арифметического выражения, заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких
# действий;
# в) Решите задачу средствами python.
# 2+2 => 4
# 1+2*3 => 7
# def multipleDivide(string: str):
#     string = string.replace('/','*/')
#     if string[0] == '*':
#         string = string[1:]   
#     splitted = string.split('*') 
#     result = 1    
#     for oneSplit in splitted:
#         if oneSplit[0] == '/':
#             result /= float(oneSplit[1:])    
#         else:
#             result *= float(oneSplit)    
#     return result

# def task3(string: str):    
#     string = string.strip()     # удаляем пробельные символы
#     string = string.replace('-','+-')
#     if string[0] == '+':
#         string = string[1:]

#     splitted = string.split('+')      
#     result = 0
#     for oneSplit in splitted:
#         result += multipleDivide(oneSplit)
#     return result        

# print(task3('2+2'))
# print(task3('1+2*3'))

# Задача 4. Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?
def task4():
    # варьируем количество быков, коров и телят
    bull_price = 100
    cow_price = 50
    calf_price = 5
    solutions = []
    for number_bulls in range(10):
        for number_cows in range(100):
            number_calf = 100 - number_bulls - number_cows
            if (bull_price * number_bulls + cow_price * number_cows + calf_price * number_calf == 1000):                    
                solutions.append([number_bulls, number_cows, number_calf])                 
    return solutions  
                    
print(task4())

