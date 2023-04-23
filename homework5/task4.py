# Создайте игру в крестики-нолики

# Таблица id игрового поля:
# | 00 | 01 | 02 |
# | 10 | 11 | 12 |
# | 20 | 21 | 22 |

# Список комбинаций id, при которых наступает выигрыш:
winList = [['00','01','02'],
           ['10','11','12'],
           ['20','21','22'],
           ['00','10','20'],
           ['01','11','21'],
           ['02','12','22'],
           ['00','11','22'],
           ['02','11','20']]

# Для множества id определяем, есть ли выигрышная комбинация
# Если есть, возвращаем ее. В противном случае return []
def checkWin(setId: set):
    for one in winList:
        if one[0] in setId and one[1] in setId and one[2] in setId:
            return one
    return []    

def printStateGameField(setId_gamerA: set, setId_gamerB: set):
    for i in range(3): 
        show = ['A ' if (str(i) + str(j)) in setId_gamerA else  \
               ('B ' if (str(i) + str(j)) in setId_gamerB else str(i) + str(j)) for j in range(3)]
        print(f'| {show[0]} | {show[1]} | {show[2]} |')

def task3():
    # Список незанятых полей:
    vacantId = set('00 01 02 10 11 12 20 21 22'.split(' '))

    # Множества полей, занимаемых игроками A, B
    setId_gamerA = set()
    setId_gamerB = set()

    # игровой цикл
    action_A = True   # очередность хода
    printStateGameField(setId_gamerA, setId_gamerB)    # Выводим состояние игрового поля
    while len(vacantId) > 0:               
        nameGamer = 'A' if action_A else 'B'
        id = input(f'> Ход игрока {nameGamer}: ')
        while id not in vacantId:
            id = input('> Вы ввели некорректное либо занятое поле. Повторите ввод: ')
        vacantId.discard(id)            
        if action_A:
            setId_gamerA.add(id)
            combination = checkWin(setId_gamerA)
        else:
            setId_gamerB.add(id)   
            combination = checkWin(setId_gamerB)
        printStateGameField(setId_gamerA, setId_gamerB)    # Выводим состояние игрового поля    

        if len(combination)>0:
            print(f'Выиграл игрок {nameGamer}, выигрышная комбинация: {combination}')
            return             
        action_A = not action_A                
    print('Игра окончена, никто не выиграл')        

task3()

