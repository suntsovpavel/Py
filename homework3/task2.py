
# Задача 2. В списке находятся названия фруктов.Выведите все фрукты, названия которых начинаются на заданную букву.
# Cписок фруктов заполните вручную.

# Считываем список фруктов из файла, чтоб не захламлять код
def readListFruits(namefile):
    with open(namefile, 'r', encoding='utf-8') as f:     
        # в строках отсекаем символ переноса
        fruits = [(line if line[-1]!='\n' else line[:-1]).lower() for line in f]
    return fruits     
        
# Выводим все фрукты, названия которых начинаются на заданную букву.       
def selectionFruits(s, fruits):
    return [fruit for fruit in fruits if len(fruit)>0 and s == fruit[0]]

s = input('Введите букву (кириллица): ').lower()
fruits = readListFruits('homework3/task2_fruits.txt')  
selection = selectionFruits(s, fruits)
print(f'Выборка фруктов, названия которых начинаются на букву {s}:\n {selection}')