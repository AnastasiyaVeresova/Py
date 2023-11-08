# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

import os
os.system("cls")

input_list = "a a a b c a a d c d d"
user_list = input_list.split()

result_list = []

for i in range(len(user_list)):
    tmp = user_list[:i].count(user_list[i])
    if tmp >= 1:
        result_list.append(f'{user_list[i]}_{tmp}')
    else:
        result_list.append(user_list[i])
    
print(input_list)
print(" ".join(result_list))



# strint_part = "a a a b c a a d c d d"
# sting_array = strint_part.split()
# string_dict = dict()
# zero = ""
# for i in sting_array:
#     if i in string_dict:
#         string_dict[i] += 1
#         zero += f"{i}_{string_dict[i]} "
#     else:
#         string_dict[i] = 0
#         zero += f"{i} "
# print(strint_part)
# print(zero)