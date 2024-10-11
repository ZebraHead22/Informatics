from random import *
from swap import swap_element

len_of_array = int(input())
my_list = [round(randint(0, 100) + random(), 2) for x in range(len_of_array)]

swap_element(my_list)



# import math

# first_frac = input().split()
# second_frac = input().split()

# def divide(frac_1, frac_2):
#   print(f'First frac is {frac_1[0]}/{frac_1[-1]}')
#   print(f'Second frac is {frac_2[0]}/{frac_2[-1]}')
#   result = [0, 0]
#   result[0], result[-1] = float(frac_1[0]) * float(frac_2[-1]), float(frac_2[0]) * float(frac_1[-1])
#   print(f'Non reduced result is {result[0]}/{result[-1]}')
  
#   def gcd(m, n):
#     while m != n:
#         if m > n:
#             m = m - n
#         else:
#             n = n - m
#     return n
  
#   n = gcd(result[0], result[-1])
  
#   if result[-1]/n != 1:
#     print(f'Reduced result is {result[0]/n}/{result[-1]/n}')
#   else:
#     print(f'Reduced result is {result[0]/n}')

# divide(first_frac, second_frac)
