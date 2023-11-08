# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import os
os.system("cls")

'''
Почему функция сортировки работает при рандомном выборе
и через раз сортирует введенное пользователем?
'''

# -------------------------функция сортировки
def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for k in range(i + 1, len(nums)):
            if nums[k] < nums[min]:
                min = k
        nums[i], nums[min] = nums[min], nums[i]


# -------------------------решение для рандомных чисел
# import random

# n = int(input('Введите кол-во элементов первого множества: '))
# m = int(input('Введите кол-во элементов первого множества: '))

# list_1 = []
# for i in range(n):
#     list_1.append(random.randint(-5, 5))
# print(list_1)

# res = set(list_1)
# print(res)

# list_2 = []
# for i in range(m):
#     list_2.append(random.randint(-5, 5))
# print(list_2)

# res2 = set(list_2)
# print(res2)


# number_intersection = res.intersection(res2)
# list_itog = list(number_intersection)

# selection_sort(list_itog)

# print()
# print(*list_itog)

# ----------------------для ввода пользователем через пробел

# n = int(input('Введите кол-во элементов первого множества: '))
# m = int(input('Введите кол-во элементов второго множества: '))

# # if n == n:
# #     for i in range(n):
# #         print('Введите через пробел элементы первого множества')
# #         list_n = input(f'{n} элементов(-а): ').split()
# #         print(list_n[0:n])
# # elif n != n:
# #     print(f'Вы ввели меньше {n} элементов(-а): ')
# #     print('Введите через пробел элементы первого множества')
# #     list_n = input(f'{n} элементов(-а): ').split()
# print('Введите через пробел элементы второго множества')
# list_n = input(f'{n} элементов(-а): ').split()
# print(list_n[0:m])

# print('Введите через пробел элементы второго множества')
# list_m = input(f'{n} элементов(-а): ').split()
# print(list_m[0:m])

# list_1 = set(list_n)
# list_2 = set(list_m)

# number_intersection = list_1.intersection(list_2)

# print(*number_intersection)
# sort_number = list(number_intersection)
# selection_sort(sort_number)

# print()
# print(*sort_number)



# --------------------------------------------------


# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# 11 6
# 2 4 12 8 3 12 10 8 6 4 2 
# 3 6 9 12 15 18 
# 6 12

# 2 5 0 1 -8 9 23 92 -8 1 5 2 9 2 6
# 7 -8 6 23 5 3 94 72 96 1


# list_n = []
# list_m = []
# for i in range(n):
#     print('Введите элементы первого множества')
#     # set_n.append(int(input(f'{n} элементов(-а): ', end=' ')))
#     list_n.append(int(input(f'{n} элементов(-а):' )))
# print(list_n)

# for i in range(m):
#     print('Введите элементы второго множества')
#     # set_m.append(int(input(f'{m} элементов(-а): ', end=' ')))
#     list_m.append(int(input(f'{m} элементов(-а): ')))
# print(list_m)


# list_1 = set(set_n.split())
# list_2 = set(set_m.split())



# для автотестов

# var1 = '5 4'
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# n = set()
# v2 = set(var2)
# v3 = set(var3)
# n = v2.intersection(v3)
# n = list(n)
# selection_sort(n)
# print(*n)



# new_list = []
# for i in var1[1:]:
#     for i in var2:
#         if i in var3:
#             new_list.append(i)
# for i in var1[:2]:
#     for i in var3:
#         if i in var2:
#            new_list.append(i)
# new_list = set(new_list)
# new_list = list(new_list)
# selection_sort(new_list)
# print(*new_list)

n = int(input('Введите кол-во элементов первого множества: '))

# можно так:
# list_n = []
# for i in range(n):
#     list_n.append(int(input(f'Введите элемент N{i + 1} первого множества: ')))
# print(list_n)

# или так:
print('Введите через пробел элементы первого множества')
list_n_2 = input(f'{n} элементов(-а): ').split()
for idx in range(len(list_n_2)):
    list_n_2[idx] = int(list_n_2[idx])
print(list_n_2)
if n != len(list_n_2):
    print(f'Вы ввели не {n} элементов(-а)')
    