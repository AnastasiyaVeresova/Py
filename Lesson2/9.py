# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while Input:       5 Output:    120


import os

os.system("cls")

# n = int(input("Введите неотрицательное число!\n"))

# if not n < 0:
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     print(result)
# else:
#     print("Вы ввели отрицательное число!")

n = int(input("Введите неотрицательное число!\n"))
i = 1
res = 1
while i <= n:
    res *= i
    i += 1
print(res)