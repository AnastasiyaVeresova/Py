# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X

import os
os.system("cls")
import random

# list_1 = [1, 2, 3, 4, 5]
# x = 6

N = int(input('Введите количество элементов в массиве: '))
list_1 = []
for i in range(N):
    list_1.append(int(input('Введите следующий  элемент: ')))
array = list(map(int, list_1))
print(array)
x = int(input('Введите число x: '))

count = 0
max = list_1[0]
min = list_1[0]
for i in range(len(list_1)):
    if list_1[i] == x:
        print(list_1[i])
if list_1[i] == x - 1:
    print(list_1[i])
elif list_1[i] == x + 1:
     print(list_1[i])

# N = int(input('Введите количество элементов в массиве: '))
# list_1 = []
# for i in range(N):
#     list_1.append(int(input('Введите следующий  элемент: ')))
# array = list(map(int, list_1))
# print(array)
# x = int(input('Введите число x: '))

# max = list_1[0]
# min = list_1[0]

# for i in range(array):
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print()
# print(min, max, i)









    
