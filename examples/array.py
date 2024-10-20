from random import *
import numpy as np


n = 3

arr = [[0]*3]*3
for i in range(n):
  arr[i] = [round(randint(0, 100) + random(), 2)] * i + [round(randint(0, 100) + random(), 2)] + [round(randint(0, 100) + random(), 2)] * (n - i - 1)

# rows, cols = 3, 3
# matrix_int = np.random.randint(0, 10, (rows, cols))
# # print(matrix_int)


for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()

print(max(arr[1]))

column_3 = list()
for i in range(n):
  for j in range(i):
    column_3.append(arr[i][2])

print(max(column_3))

#Функции генераторы
#Подход 2
def generate_squares(n):
  for x in range(n):
    yield x**2

for i in generate_squares(5):
  print(i, end=' | ')

gen = generate_squares(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#Подход 1
l = [1, 2, 3, 4, 5]
iter_list = iter(list(map(lambda x: x**2, l)))

print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
