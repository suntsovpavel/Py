# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. 
# Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# Результат: 8x^2 +4x + 8

# чистим строку от пробельных символов:
def clearSpaceSymbols(string):
    result = ''
    for s in string:
        if not s.isspace():
            result += s
    return  result           

#возвращаем массив индексов вхождений подстроки substr в строку string
def getIndexesSubstr(string, substr):
    return [i for i in range(len(string)) if string.startswith(substr, i)]

# Парсим файл и возвращаем первую строку
def getFirstLineFromFile(namefile):
    data = open(namefile, 'r', encoding='utf-8')
    lines = data.readlines()
    if len(lines) == 0:
        print(f'!!!error, file {namefile} is empty!!!')
    else:        
        return lines[0]        

# Парсим строку с записью многочлена. Формат:  3x^2 + 1.5x + 8
# возвращаем кортеж (dict_, messageError), где
# dict_: словарь, где ключ N: степень полинома, значение: коэффициент при x^N
# (либо их сумма, если в строке несколько слагаемых с x^N)
# messageError: сообщение об ошибке. Если ошибки нет, возвращаем None 
def parsePolynomial(string):
    if len(string) == 0 or string.isspace():
        return {}, f"задана пустая строка '{string}'"
    
    stringPrimary = string  # сохранка для печати
    
    # Удаляем из строки все пробельные символы
    #for s in ' \t\n':
    #    string = string.replace(s,'')
    string = clearSpaceSymbols(string)
        
    string = string.replace('-','+-')    # заменяем в строке все минусы на '+-':  
    if string[0] == '+':        
        string = string[1:]     # Если этого не сделать, в string.split('+') получим лишний сплит-пустышку      
    
    splitted = string.split('+')      
    
    # Приводим члены со степенями 1 и 0 к виду 'x^1' и 'x^0':
    for i in range(len(splitted)):   
        if len(splitted[i]) == 0:
            return {}, f"'в splitted найдена пустышка: {splitted}'; исходная строка '{saveString}'"
        
        # список включений 'x' в текущем сплите:
        indexes = getIndexesSubstr(splitted[i], 'x')
        if len(indexes)>1:
            return {}, f"в '{splitted[i]}' имеется более одного 'x'; исходная строка '{saveString}'"
        
        if not 'x^' in splitted[i]:
            if len(indexes) == 0:
                # сплит, в котором свободный коэффициент.Приклеиваем 'x^0' справа:
                splitted[i] += 'x^0'                   
            else:
                # сплит x в степени 1(просто 'x'), который мы меняем на 'x^1'                                 
                splitted[i] = splitted[i].replace('x','x^1')
    print(f"Полином в представлении 'x^N': '{'+'.join(splitted)}'")                        

    dictResult = {}
    # Формируем словарь 'степень полинома':'коэффициент'
    for oneSplite in splitted:
        # на всякий случай проверка:
        if not 'x^' in oneSplite:
            return {}, f"во вложении '{oneSplite}' отсутствует 'x^'; исходная строка '{stringPrimary}'"
        pair = oneSplite.split('x^')  # 2 значения: коэффициент и степень полинома
        if len(pair[0]) == 0:
            coefficient = 1.
        elif pair[0] == '-':
            coefficient = -1.
        else:
            coefficient = float(pair[0])
        degreePolynomial = int(pair[1]) 
        
        if degreePolynomial in dictResult.keys():
            # складываем coefficient с уже имеющимся значением
            dictResult[degreePolynomial] += coefficient
        else:
            dictResult[degreePolynomial] = coefficient           
    return dictResult, None            
        
# print(parsePolynomial(getFirstLineFromFile('task4_data2.txt')))

# по данным двух словарей 'степень полинома':'коэффициент' 
#  формируем полином с суммирующими коэффициентами в виде строки
def summaryPolynomial(dict1, dict2, eps: float = 1.e-9):
    # Добавляем в словарь dict1 содержимое dict2
    # Для равных ключей содержимое словарей суммируется
    for key in dict2.keys():
        if key in dict1.keys():
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]            
    
    # Формируем суммарный полином-строку
    result = ''
    for key in dict1.keys():
        if abs(dict1[key]) > eps:
            result += str(dict1[key]) + 'x^' + str(key) + '+'            
    
    if len(result)>0 and result[-1] == '+': 
        result = result[:-1]        
    result = result.replace('+-','-')
    result = result.replace('x^1','x')
    result = result.replace('x^0','')
    # result = result.replace('+',' + ')
    # result = result.replace('-',' - ')
    return result

def task4():   
    line1 = getFirstLineFromFile('homework4/task4_data.txt')
    dict1, messageError = parsePolynomial(line1)   
    if messageError != None:
        print(messageError)
        return
    line2 = getFirstLineFromFile('homework4/task4_data2.txt')
    dict2, messageError = parsePolynomial(line2)       
    if messageError != None:
        print(messageError)
        return
    print(f"Исходные полиномы: '{line1}', '{line2}'")
    print(f'Итоговый полином: {summaryPolynomial(dict1, dict2)}')    
    
task4() 
            