class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Выполняем вращение
        x.right = y
        y.left = T2

        # Обновляем высоты
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Выполняем вращение
        y.left = x
        x.right = T2

        # Обновляем высоты
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, value):
        # Выполняем стандартную вставку как в бинарном дереве поиска
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        # Обновляем высоту текущего узла
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Проверяем баланс текущего узла
        balance = self.get_balance(node)

        # Если узел стал несбалансированным, выполняем соответствующее вращение
        # Левый левый случай
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Правый правый случай
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Левый правый случай
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Правый левый случай
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pre_order(self, root):
        if not root:
            return
        print(root.value, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)

# Пример использования
tree = AVLTree()
root = None

# Вставка элементов
elements = [10, 20, 30, 40, 50, 25]
for element in elements:
    root = tree.insert(root, element)

# Печать элементов дерева в прямом порядке
print("Pre-order traversal of the AVL tree:")
tree.pre_order(root)  # Вывод: 30 20 10 25 40 50
