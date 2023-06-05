# Необходимо превратить собранное на семинаре дерево поиска 
# в полноценное левостороннее красно-черное дерево 
# и реализовать в нем метод добавления новых элементов с балансировкой.

# Красно-черное дерево имеет следующие критерии:
# • Каждая нода имеет цвет (красный или черный)
# • Корень дерева всегда черный
# • Новая нода всегда красная
# • Красные ноды могут быть только левым ребенком
# • У краcной ноды все дети черного цвета

# Соответственно, чтобы данные условия выполнялись, 
# после добавления элемента в дерево необходимо произвести балансировку, 
# благодаря которой все критерии выше станут валидными. 
# Для балансировки существует 3 операции – левый малый поворот, правый малый поворот и смена цвета.

# Код реализован для value тип int

class Node:
    # конструктор 
    def __init__(self, 
                 value: int,  
                 isRed: bool = True,    # по умолчанию добавляется узел красного цвета
                 left = None,
                 right = None):
        self.value = value
        self.isRed = isRed     # True: красный, False: черный
        self.left = left
        self.right = right    
        
    # def copyTo(self, 
    #            other):
    #     other.value = self.value
    #     other.isRed = self.isRed
    #     other.left = self.left                            
    #     other.right = self.right
        
    # Для потомков возвращаем value, если ссылка не None, иначе 'None'        
    def print(self):
        print(f"""(value={self.value}, color={
              'red' if self.isRed else 'black'}, left={
              self.left.value if self.left else 'None'}, right={                                                             
              self.right.value if self.right else 'None'})""")                
        
class BinarySearchTree: 
    def __init__(self, 
                 root: Node = None):
        self.__root = root
        
    # См.схему рисунок А
    def __rightSwap(self,
                  node: Node):
        rightChild = node.right
        (node.right, rightChild.left) = (rightChild.left, node)        
        rightChild.isRed = node.isRed
        node.isRed = True
        return rightChild    
    
    # См. схему рисунок Б
    def __leftSwap(self,
                 node: Node):
        leftChild = node.left
        (node.left, leftChild.right) = (leftChild.right, node)
        leftChild.isRed = node.isRed
        node.isRed = True
        return leftChild    
    
    # См. схему рисунок В
    def __colorSwap(self,
                  node: Node): 
        node.right.isRed = False
        node.left.isRed = False
        node.isRed = True
        
    def __rebalance(self,
                  node: Node):
        needRebalance = True
        while needRebalance:
            needRebalance = False
            # Если правый ребенок – красный, применяем малый правый поворот
            if (node.right and node.right.isRed):   #and (not node.left or not node.left.isRed)):
                needRebalance = True
                node = self.__rightSwap(node)
            
            # Если левый ребенок красный и его левый ребенок тоже красный 
            # – применяем малый левый поворот
            if (node.left and node.left.isRed and 
                node.left.left and node.left.left.isRed):                 
                needRebalance = True
                node = self.__leftSwap(node)
            
            # Если оба ребенка красные – делаем смену цвета
            if (node.left and node.left.isRed and  
                node.right and node.right.isRed):
                needRebalance = True
                self.__colorSwap(node)                                        
        return node
                                                  
    def __addNode(self, 
                node: Node,      # узел, к которому добавляем потомка
                value: int):            
        if node.value == value:
            return False
        elif node.value > value:    # добавляем слева
            if node.left:
                result = self.__addNode(node.left, value)
                node.left = self.__rebalance(node.left)
                return result
            else:
                node.left = Node(value)     # isRed = true                                    
                return True
        else:                       # добавляем справа
            if node.right:
                result = self.__addNode(node.right, value)
                node.right = self.__rebalance(node.right)
                return result
            else:
                node.right = Node(value)    # isRed = true        
                return True               

    def add(self, 
            value: int):
        if self.__root:            
            result = self.__addNode(self.__root, value)
            self.__root = self.__rebalance(self.__root)
            self.__root.isRed = False
            return result
        else:
            self.__root = Node(value,
                        False) # isRed
            return True                         
        
    def __printWithChildren(self, 
                     node: Node):
        node.print()    # в вызывающем коде уже проверили, что node != None
        if node.right:
            self.__printWithChildren(node.right)            
        if node.left:            
            self.__printWithChildren(node.left)                      
        
    def print(self):
        if self.__root:
            self. __printWithChildren(self.__root)                                        

# using code
# 1. С последовательным заполнением от 1 до 10:
tree = BinarySearchTree()
for i in range(1, 11):
    tree.add(i)    
print('1. С последовательным заполнением от 1 до 10:')    
tree.print()

# 2.  С последовательным заполнением от 10 до 1:
tree = BinarySearchTree()
for i in range(10, 0, -1):
    tree.add(i)
print('2. С последовательным заполнением от 10 до 1:')    
tree.print()    

#see readme.md
    
    


        
        