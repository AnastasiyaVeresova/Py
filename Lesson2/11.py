# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1. Input:     5 Output:  6

import os
os.system("cls")

# n = int(input("Введите число: "))
# a = 1
# b = 0
# i = 1
# fibonacci = 0
# count = 0

# while i <= n + 1:
#     # print(fibonacci, end=" ")
#     if fibonacci == n:
#         # print(f"\nЧисло {n} по счету на {i} месте")
#         break
#     fibonacci = a + b
#     a = b
#     b = fibonacci
#     i += 1
# else:
#     i = -1
# print(i)

A = int(input('Введите число: '))
num1, num2, n = 0, 1, 2
while num2 < A:
    num1, num2 = num2, num1 + num2
    n += 1
if num2 == A:
    print (n)
elif num2 - A < A - num1:
    print(f'Да, оно не входит в ряд Фибоначчи, но ближайшее число {num2}')
elif num2 - A > A - num1:
    print(f'Да, оно не входит в ряд Фибоначчи, но ближайшее число {num1}')
else:
    print(f'Да, оно не входит в ряд Фибоначчи, но ближайшие числа {num1} и {num2}')
    

        
