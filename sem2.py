# Задача 0. Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный.
# 	10 -> 10 (чётный), 5(нечётный), 2 (чётный), 1(нечётный)

# явное указание типа num !!!!!!!!!!!!!
def check(num: int):
    if num % 2 == 0:
        return('четное')
    else:
        return('нечетное')  

def task1():
    num = int(input('Введите число: '))

    # count = 1
    # while count <= num:
    #     print(count)
    #     count += 1

    print(range(num))
    # range(0, 6)  = поулинтервал [0,6])
    for i in range(1, num+1):
        if num % i == 0:
             print(f'{i} {check(i)}')       
 
# Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.
def task2():
    for x in range(2):
        for y in range(2):
            print(f'{x} {y} {not x and y}')    

# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другую.     
def task3(str, str2):
    count = 0
    for i in range(len(str2)-len(str)+1):
        # print(str, str2[i:i+len(str)])
        if str == str2[i:i+len(str)]:            
            count += 1
    return count            
# print(task3('qwe', 'qwertyqwe'))

# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
def task4(num):
    numbers = []
    for i in range(num):
        numbers.append((-3)**i)
    print(numbers)
# task4(int(input('Введите число: ')))

# Задача 4. Найдите все числа до 10000, у которых количество делителей равно 10.
def subtask5(num: int):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1    
    return count
def task5():
    for i in range(1,10001):
        if subtask5(i) == 10:
            print(f'{i}\t ', end='')
task5()