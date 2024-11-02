'''Односвязный список
Структура узла

Каждый узел односвязного списка обычно состоит из двух частей:

Данные: Содержит значение, которое хранится в узле.
Ссылка на следующий узел: Указывает на следующий элемент списка.
Операции с односвязным списком

Добавление узла в начало списка:
Создаем новый узел.
Связываем его с текущим первым элементом списка.
Новый узел становится первым элементом списка.
Добавление узла в конец списка:
Проходим по списку до конца.
Связываем последний узел с новым узлом.
Удаление узла:
Чтобы удалить узел, нужно изменить ссылку предыдущего узла, чтобы он указывал на узел после удаляемого.
Поиск элемента:
Проходим по каждому узлу и проверяем значение.'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(3)
ll.append(5)
ll.prepend(1)
ll.display()  # Вывод: 1 -> 3 -> 5 -> None
ll.delete_value(3)
ll.display()  # Вывод: 1 -> 5 -> None

'''Двусвязный список
В двусвязном списке каждый узел хранит ссылки как на следующий, так и на предыдущий узлы, что позволяет более гибко перемещаться по списку. 
Это дает некоторые преимущества при удалении узлов или обходе списка в обратном порядке, хотя и занимает больше памяти.'''

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = DoubleNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")
