
# Задача 2. В первом списке находится информация об ассортименте мороженого, 
# во втором списке - информация о том, какое мороженое есть на складе. 
# Выведите названия того товара, который закончился.
# 1.«Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2.«Сливочное», «Вафелька», «Сладкоежка». 
# Ответ: Закончилось: «Бурёнка»
     
string1 = '«Сливочное» «Бурёнка» «Вафелька» «Сладкоежка»'  # ассортимент продукции
string2 = '«Сливочное» «Вафелька» «Сладкоежка»'          # то, что имеется на складе

print(f'Ассортимент продукции: {string1}')
print(f'В наличии на складе: {string2}')

setA = set(string1.split(' '))
setB = set(string2.split(' '))    
    
difference = setA.difference(setB) 
if len(difference) > 0:            
    print(f'Закончилось: {difference}')    
else:            
    print('Все позиции товара в наличии') 