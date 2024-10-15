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