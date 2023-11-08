# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure.So if she sells sea shells on the sea shore
# I'm sure that the shells are sea shore shells
# Output: 13

import os
os.system("cls")

s = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''

# # s_list = set(s.lower().replace('sure.so', 'sure so').replace('i\'m', 'i am').split())
# # print(s_list)
# # print(len(s_list))

# def multiple_replace(target_str, replace_values):
#     for i, j in replace_values.items():
#         target_str = target_str.replace(i, j)
#     return target_str

# replace_values = {'.': ' ', '-': ' '}

# print('Введите текст:') #Жили-БЫЛИ.Ели-пили-пили
# text = input()
# text1 = multiple_replace(text, replace_values)
# text_set = set(text1.lower().split())
# print(text_set)
# print(len(text_set))


# ---------------------------------------------------------------

list_string = s.replace(".", " ").lower().split()
print(s)
print(len(set(list_string)))