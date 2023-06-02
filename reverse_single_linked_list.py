
# Узел односвязного списка: значение + ссылка на следующий узел
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Отдельный класс списка не создаем
# В качестве списка передаем ссылку на начальный узел Node
# Замыкающий узел имеет ссылку self.next = None

# Вывод списка
# Пробегаемся по узлам, пока head.next не None
def print_list(begin_msg: str, head: Node, end='\n'):
    print(begin_msg, end='')
    while head: 
        print(head.data, end=' -> ' if head.next else '')
        head = head.next    
    print(end=end)

# Реверс (разворот) списка
def reverse_list(head, tail=None):
    while head:
        # Для каждой пары узлов A,B:
        # До выполнения инструкции: head указывает на A, A.next - на B, 
        #   tail - на узел слева от A (если A - начальный узел, tail=None)
        # После инструкции:  A.next указывает на узел слева от A, tail - на A, 
        #   head - на B (Если А - замыкающий узел списка, head=None)
        head.next, tail, head = tail, head, head.next
    return tail

# using code
# 1. Создаем список в виде последовательности узлов
head = Node(1, Node(2, Node(3, Node(4))))
print_list('Исходный список: ', head)

# 3. Разворот
reversed_list = reverse_list(head)
print_list('Развернутый список: ', reversed_list)

# Результат выполнения:
# Исходный список: 1 -> 2 -> 3 -> 4
# Развернутый список: 4 -> 3 -> 2 -> 1    