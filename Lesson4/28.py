#  Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы. 2 2  4

import os
os.system("cls")

a = 3
b = 5

# def sum(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return sum(a, b)
#     else:
#         return a
    
# print(sum(a, b))

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a + 1, b - 1)
print(sum(a, b))

