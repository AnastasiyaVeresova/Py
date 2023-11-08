#  Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)

import os

os.system("cls")

res = 0
n = int(input("Введите трехзначное число "))
while n > 0:
    digit = n % 10
    if digit != 0:
        res += digit
    n = n // 10

print(res)

n = input("Введите трехзначное число ")
res = 0
for i in n:
    i = int(i)
    res += i
print(res)

# n = int(input("Введите трехзначное число "))
# digit1 = n // 100
# digit2 = (n % 100) // 10
# digit3 = n % 10
# res = digit1 + digit2 + digit3
# print(res)