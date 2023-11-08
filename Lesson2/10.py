#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть. 5 -> 1 0 1 1 0 2

import os

os.system("cls")

quantityCoins = int(input("Введите количество монет: "))
import random

coins = []
for i in range(quantityCoins):
    coins.append(random.randint(0, 1))
    print(coins)

sum1 = 0
sum2 = 0
coins = [0, 1, 0, 1, 1, 0]
for i in range(len(coins)):
    if coins[i] == 0:
        sum1 += 1
    elif coins[i] == 1:
        sum2 += 1
print(coins)
if sum1 >= sum2:
    print(f"Нужно перевернуть {sum2} орла (-ов)")
else:
    print(f"Нужно перевернуть {sum1} решек (-у)")

