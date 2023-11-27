import os
os.system("cls")

import pandas as pd

# def add_contact():
#     file_name = 'phone_book.txt'
#     data = 'Иванов, Иван, Иванович, 1234567'

#     # file = open(file_name, 'w', encoding='utf-8')
#     # file.write('123')
#     # file.close()

#     with open(file_name, 'w', encoding='utf-8') as fd:
#         fd.write(data)

# def read_file():
#     file_name = 'phone_book.txt'
#     new_file = 'new_phone_book.txt'
#     try:
#         with open(file_name, 'r', encoding='utf-8') as fd:
#             data = fd.readlines()
#             # print(data)
#             for idx, val in enumerate(data):
#                 # print(f'{idx = }, {val = }')
#                 print(f'{idx}) {val.rstrip()}')
#             ind_str = input('Введите необходимый индекс: ')
#             try:
#                 ind = int(ind_str)
#                 # if 0 <= ind < len(data):
#                 #     print(f'{data[ind]}\n')
#                 #     with open(new_file, 'w', encoding='utf-8') as f:
#                 #         f.write(f'{data[ind]}\n')
#                 try:
#                     print(f'{data[ind]}\n')
#                     with open(new_file, 'w', encoding='utf-8') as f:
#                         f.write(f'{data[ind]}\n')
#                 except IndexError:
#                     print('Вы ввели несуществующий индекс')
#             except ValueError:
#                 print('Надо ввести целое число')


#     except FileNotFoundError as err:
#         print('Файл еще не создан, введите данные', err)


# read_file()
# # add_contact()






phone = '7934795737545'

lines = ['Лесопарковый Бушрут Замшелович, тел.: 895674536, 84765455456']

text = lines[0]
print(''.join(text[text.find('тел.:') + 6:] + ', ' + phone ))
print(lines)
print(phone + ', ' + text[text.find('тел.:') + 6:])

#------------------------------------------------------------------------------------
# lines = ['Лесопарковый Бушрут Замшелович, тел.: 895674536, 84765455456']

# headers = ['Фамилия', 'Имя', 'Номер телефона']
# contact_list = []
# for line in lines:
#     line = line.strip().split()
#     contact_list.append(dict(zip(headers, line)))

# print(contact_list)
# [{'Фамилия': 'Лесопарковый', 'Имя': 'Бушрут', 'Номер телефона': 'Замшелович,'}]


pd.DataFrame()
