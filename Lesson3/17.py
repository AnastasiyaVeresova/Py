# Дан список чисел. Определите, сколько в нем встречается различных чисел. Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.   5      1 2 3 4 5      6-> 5

# list_num = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_num)))
# print(set(list_num))
# from random import randint

import os

os.system("cls")

# list_num = [1, 1, 2, 0, -1, 3, 4, 4]

# count = 0
# new_list = []
# for i in list_num:
#     if i not in new_list:
#         new_list.append(i)
# print(len(new_list))
# print(new_list)

digits = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(digits)))