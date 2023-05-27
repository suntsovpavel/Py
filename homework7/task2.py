# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def wrapper(count: int):
    def stopwatch(func):
        def decorator():
            for _ in range (count):
                func()
        return decorator   
    return  stopwatch   

@wrapper(int(input('Введите количество раз вызова функции: ')))
def our_hello_world():
    print('Hello World!')

our_hello_world()
