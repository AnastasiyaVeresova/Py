# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X   5       1 2 3 4 5        3-> 1

import os

os.system("cls")

N = int(input('Введите количество элементов в массиве: '))
list_N = input('Введите элементы списка через пробел: ').split()
array = list(map(int, list_N))
x = int(input('Введите число x: '))
count = 0
for i in range(N):
    if array[i] == x:
        count += 1
print(f'Число {x} встречается в списке {count} раз(-а)')