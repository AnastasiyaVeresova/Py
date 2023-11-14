# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива Ввод: Вывод: 7 3 3 2 12 3 1 3 4 2 4 12 6 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

print(sp:=[random.randint(1,10) for _ in range(10)])
print(sp1:=[random.randint(1,10) for _ in range(5)])
sp1 = set(sp1)
result = []
for i in sp:
    if i not in sp1:
        result.append(i)
print(result)
print(result2:=[i for i in sp if i not in set(sp1)])


##-------------------------------------------------------

# def filter_list(array1, array2):
#     res_array = []
#     for i in array1:
#         if i not in array2:
#             res_array.append(i)
#     return res_array

# def create_random_list(number):
#     return [random.randint(-10,10) for _ in range(number+1)]

# number_1 = int(input("Введите количество элементов первого массива: "))
# int_array_1 = create_random_list(number_1)
# print(int_array_1)
# number_2 = int(input("Введите количество элементов второго массива: "))
# int_array_2 = create_random_list(number_2)
# print(int_array_2)
# print(filter_list(int_array_1, int_array_2))
