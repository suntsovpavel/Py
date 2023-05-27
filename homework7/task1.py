# Задача 1. Создайте пользовательский аналог метода map().

def our_map(func, numbers):
    return (func(el) for el in numbers)

# using code
numbers = [0,1,2,3,4,5]
print(list(our_map(lambda x: x*x, numbers)))
