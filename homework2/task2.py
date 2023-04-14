# Задача 2. Выведите таблицу истинности для выражения
# ¬(X ∧ Y) ∨ Z.

def task2():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                result = not (x and y) or z
                print(f'x: {x}, y: {y}, z: {z}, result: {result}')  
task2()                