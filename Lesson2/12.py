# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. 4 4 -> 2 2 5 6 -> 2 3

import os

os.system("cls")

# numberX = int(input("Введите число X "))
# numberY = int(input("Введите число Y "))
# temp = 0
# if numberX > numberY:
#     temp = numberY
#     numberY = numberX
#     numberX = temp
# if numberX > 1000 or numberY > 1000:
#     print("Неверно заданы параметры")
# else:
#     for x in range(numberX):
#         for y in range(numberY):
#             if numberX == x + y and numberY == x * y:
#                 first_num = y
#                 second_num = x
# print(f"{first_num} {second_num}")



# x = (int(input("Первое число: ")))
# y = (int(input("Второе число: ")))

# sum = x + y
# sum = (int(input("Сумма чисел: ")))
# print(f'Сумма чисел: {x + y}')
# multiplicate = x * y
# print(f'Произведение чисел: {x * y}')
# multiplicate = (int(input("Произведение чисел: ")))
# if multiplicate == 0: print(sum, 0)
# else:
#     for i in range(1, sum // 2 + 1):
#         if (multiplicate % i == 0) and (sum - i == multiplicate / i):
#             print (i, sum - i, end="\n")



# s = int(input("Сумма чисел: "))
# m = int(input("Произведение чисел: ")) 
# for x in range(s):
#     for y in range(s):
#         if x + y == s and x * y == m:
#             print(x, y, end=' ')

s = int(input("Сумма чисел: "))
p = int(input("Произведение чисел: ")) 
solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1])