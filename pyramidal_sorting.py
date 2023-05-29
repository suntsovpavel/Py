# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в array[]. n - размер кучи
def heapify(array, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and array[i] < array[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and array[largest] < array[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        array[i],array[largest] = array[largest],array[i]  
        heapify(array, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(array):
    n = len(array)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]   
        heapify(array, i, 0)

# using code
numbers = [ 12, 11, 13, 5, 6, 7]
heapSort(numbers)
print("Sorted arrayay is: ")
for one in numbers:
    print(f'{one}\t', end='')
