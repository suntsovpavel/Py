# Задача 3. Даны две строки. Посчитайте сколько раз
# каждый символ первой строки встречается во второй
# «one» «onetwonine»:
# o – 2, n – 3, e – 3

def countSymbolInString(symbol, str):
    count = 0
    for s in str:
        if s == symbol:
            count += 1  
    return count          

str = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
print([countSymbolInString(s, str2) for s in str])