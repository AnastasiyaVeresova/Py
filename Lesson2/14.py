# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. 10 -> 1 2 4 8

import os

os.system("cls")

n = int(input("Введите число "))
for x in range(0, n, 1):
    p = 2 ** x
    if p <= n:
        print(p, end=' ')


# n = int(input("Введите число "))
# k = 0
# while 2 ** k <= n:
#     print(2 ** k, end=' ')
#     k += 1

