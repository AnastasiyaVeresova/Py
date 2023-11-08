# Задача VERY HARD необязательная
# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8
import os
os.system("cls")

from itertools import groupby

list = [1, 5, 2, 7, 7, 4, 3, 1, 7, 8 , 15 , 1 ]
print(list)

list.sort()
print(list)

for key, group in groupby(enumerate(list), lambda i_x:i_x[0]-i_x[1]):
    print([x for i, x in group], end=", ")
##---------------------------------------------------------------------------------

for item in range(0, len(list), 1):
    length1 = []
    length1.append(item)
    print(length1)

# for i in range(len(list)):
#     min = i
#     for k in range(i + 1, len(list)):
#         if list[k] < list[min]:
#             min = k
#     list[i], list[min] = list[min], list[i]

# length1 = []
# length2 = []






# print(list)


# for i in range(len(list)-1):
#     if list[i] == list[i+1] - 1:
#         length1.append(list[i])
#         i += 1
#     elif list[i] < list[i+1] - 1:
#         length2.append(list[i])

# print(f'1: ', length1)
# print(f'2: ', length2)

# print(len(length1))

# print(f'2: ', length2)

# print(f"all: {length1}, {length2}, {[list[-1]]}")

##---------------------------------------------------------------------------------------

# current_length = 1
# max_length = 1

# current_index = 0
# max_index = 0

# for i in range(1, len(list)):
#     if list[i] > list[i-1]:
#         current_length += 1
#     else:
#         if current_length > max_length:
#             max_length = current_length
#             max_index = current_index
#         current_length = 1
#         current_index = i
# if current_length > max_length:
#     max_length = current_length
#     max_index = current_index

# result = list[max_index:max_index+max_length]
# print(result)

 

# def find_longest_sequence(list):
#     longest_sequence = []
#     current_sequence = []
#     for num in list:
#         if not current_sequence:
#             current_sequence.append(num)
#         elif num > current_sequence[-1]:
#             current_sequence.append(num)
#         else:
#             if len(current_sequence) > len(longest_sequence):
#                 longest_sequence = current_sequence
#             current_sequence = [num]
#     if len(current_sequence) > len(longest_sequence):
#         longest_sequence = current_sequence
#     return longest_sequence
# list = [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ]
# result = find_longest_sequence(list)
# print(result)




# def get_up2(list):
#     ups = [list[0]]
#     for i in list:
#         if i > max(ups):
#             ups.append(i)
#     return ups
# print(get_up2(list))


