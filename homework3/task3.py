
import random

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

# На каждый запрос бот имеет несколько вариантов ответа, выбираемых случайным образом.
# Пользователь может добавлять варианты ответов в диалоге через звездочку, пример:
# >привет
# привет!
# >*Здорово!
# /список ответов на "привет" дополнен вариантом "Здорово!"/

# Если запрос не имеется в словаре, бот отвечает 'Не могу ответить. Как бы ответил ты?',
# и сохраняет в словарь запрос-ответ пользователя 

# После завершения диалога файл словаря бота перезаписывается с учетом добавлений

# Считываем словарь из файла
def parseFileDataBot(namefile):
    dictionary = {}
    with open(namefile, 'r', encoding='utf-8') as f:     
        for line in f:            
            if line[-1] == '\n':    # отсекаем символ переноса
                line=line[:-1] 
            splitted = line.split(':')
            dictionary[splitted[0]] = splitted[1].split('&')  # список из нескольких вариантов ответа                              
    return dictionary

# Записываем словарь в файл
def writeFileDataBot(namefile, dictionary):
    with open(namefile, 'w', encoding='utf-8') as f:
        for key in dictionary.keys():
            line = key + ':' + '&'.join(dictionary[key]) + '\n' 
            f.write(line)                  
                 
# Чтобы не сломать формат записи файла, 
# удаляем из фраз, вводимых пользвателем, разделители ':' и '&', заменив их пробелами    
delimiters = ':&'       
def filterInput(string):
    result = ''
    for s in string:
        result += (s if s not in delimiters else ' ')            
    return result            
            
def initChat(namefile):
    dictionary = parseFileDataBot(namefile)
    print(f'Словарь успешно считан из {namefile}')
    # print(dictionary)
    messageUser = ''
    keyLatest = ''  # сохранка последнего запрошенного ключа
    expectedKey = True  #True: ожидается ввод ключа, False: ожидается ввод значения (пополнение списка возможных ответов бота)
    isNewName = False
    print("Чтобы закончить диалог, введите 'стоп'")
    print("Чтобы добавить вариант ответа бота на текущий запрос, введите '*', а затем текст")
    while messageUser != 'стоп':
        messageUser = filterInput(input('> '))   # filterInput: заменяем пробелами введенные символы ':' и '&'

        if len(messageUser) > 0 and messageUser[0] == '*':   # ожидается ввод значения (пополнение списка возможных ответов бота)
            messageUser = messageUser[1:]
            expectedKey = False    

        if len(messageUser) == 0 or messageUser.isspace():
            print('//введена пустая строка')             

        elif messageUser.lower() == 'стоп':
            writeFileDataBot(namefile, dictionary)
            print('До свидания, всего наилучшего!')        
            print(f'//Файл словаря бота "{namefile}" перезаписан') 

        else:
            if expectedKey:  # ожидается ввод ключа
                keyLatest = messageUser.lower()          
                if messageUser.lower() in dictionary.keys():                                                                      
                    answers = dictionary[messageUser.lower()]                       
                    if len(answers) == 1:                                                
                        print(answers[0])                            
                    else:                        
                        print(answers[random.randint(0, len(answers)-1)])    
                else:
                    isNewName = True        
                    print('Не могу ответить. Как бы ответил ты?') 
                    expectedKey = False  # переключаемся в режим ввода значения
            else:   # ожидается ввод значения: пополнение списка возможных ответов бота на текущий запрос keyLatest (isNewName=False)
                    #   либо значение вновь добавлемой пары (isNewName=True)
                if keyLatest == '':
                    print('//Не было сделано ни одного запроса ключа/')    
                else:    
                    if isNewName:                            
                        dictionary[keyLatest] = [messageUser] 
                        print(f"//в словарь добавлена пара: '{keyLatest}' : '{messageUser}'")
                        isNewName = False
                    else:  
                        if messageUser not in dictionary[keyLatest]:                           
                            dictionary[keyLatest].append(messageUser)  
                            print(f'//список ответов на "{keyLatest}" дополнен вариантом "{messageUser}"')
                        else:
                            print('//такой вариант ответа уже имеется')   
                expectedKey = True    # переключаемся в режим ввода ключа       
    
initChat('homework3/task3_dataBot.txt')    