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


# pd.DataFrame()

#----------------------------------------------

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
# print(data)


# name_one = ['robot', 'human']
# name_two = ['1', '0']
# list = list(zip(name_one, name_two))

# print(list)

# dframe = pd.DataFrame(list, columns = ['robot', 'human'])
# print(dframe)


# d = {'robot' : pd.Series([0], index = [0]), 'human': pd.Series([1], index = [1])}
# dframe = pd.DataFrame(d)
# print(dframe)

# data = {
#     'robot' : ['0'],
#     'human' : ['1']
#     }
# row_labels = [0, 1]

# df = pd.DataFrame(data=data, index = row_labels)
# print(df)

# data.loc[data['WhoAmI']] == 'human', 'human' = '1'
# data.loc[data['WhoAmI']] == 'robot', 'robot' = '0'
# data.drop(columns='"WhoAmI')

# data = pd.DataFrame(random.sample(['robot', 'human'] * 10, 10), columns = {'WhoAmI'})
# data.head()
# print(data)

# data = pd.DataFrame(np.arrange(16).reshape(4, 4), index = list('0', '1'), columns = list('robot', 'human'))
# print(data)
#--------------------------------------
# df1 = pd.DataFrame({'robot': [random.randint(0, 1)]})
# df2 = pd.DataFrame({'human': [random.randint(0, 1)]})


# df1.merge(df2, how='cross')

# print(df1)
#---------------------------------
# data = {
#     'robot' : [0],
#     'human' : [1],
#     }

# row_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# df = pd.DataFrame(data=data, index = row_labels)
# print(df)

#---------------------------------















































# ####===========================================================================

# import os
# import re
# #========================================================Функция для подсчета строк в файле

# def count_nonempty_lines(file_name):
#     if os.path.exists(file_name):
#         with open(file_name, 'r', encoding='utf-8') as f:
#             return len([line for line in f if line.rstrip()])
#     else:
#         return 0
# ##============================================для подсчета
#     # with open('phone_book/phonebook.txt', 'r', encoding='utf-8') as source:
#     #     count = 0
#     #     s = source.readline()
#     #     while s != '':
#     #         s=source.readline()
#     #         count += 1
#     # print(count)
#     # source.close()
# #========================================================Функция для удаления   

# def remove(file_name:str):
#     file_name = 'phone_book/phonebook.txt'
#     flag_exit = False
#     while not flag_exit:
#         for_remove = input('Выберите:\n1 - для удаления определенного контакта по порядковому номеру\n2 - для полного очищения телефонного справочника\nx - для выхода: ')
#         print()
#         if for_remove == '1':
#             with open(file_name, 'r', encoding='utf-8') as main:
#                 with open('phone_book/backup_file.txt', 'w', encoding='utf-8') as copy:
#                     for i, line in enumerate(main, 1):
#                         copy.write('{}: {}'.format(i, line))
#                         print(f'{i}.', line.rstrip())
#                     print()
#                     copy.close()
#                     main.close()
#                     position_delete = int(input('Введите № позиции для удаления: '))
#                     try:
#                         with open(file_name, 'r', encoding='utf-8') as source:
#                             content = source.read()
#                             lines = content.splitlines()
#                             del lines[position_delete - 1]
#                             new_content = '\n'.join(lines)
#                         with open(file_name, 'w', encoding='utf-8') as source:
#                             source.write(new_content)
#                             source.close()
#                         print("Контакт удален")
#                         print()
#                     except:
#                         print("Ошибка")
#         elif for_remove == '2':
#             try:
#                 open(file_name, 'w').close()
#                 print("Телефонная книга успешно очищена")
#                 print()
#             except:
#                 print("Ошибка")
#         elif for_remove == 'x':
#             flag_exit = True

# #========================================================Функция для показа всех записей в справочнике
# def show_all(file_name:str):
#     if count_nonempty_lines(file_name) == 0:
#         print('Телефонная книга пуста > выберите 2 для добавления контакта')
#         print()
#     else:
#         print('Список ваших контактов: ')
#         with open(file_name, 'r',encoding='utf-8') as f:
#             data = f.readlines()
#             # op = f.readline()
#             i = 0
#             for lines in data:
#                 if len(lines) > 1:
#                     i += 1              
#                     print(str(i) + '. ' + lines.rstrip()) 

#             print()
#             # file_name.close()

# #========================================================Функция для добавления нового контакта

# def add_new(file_name):
#     try:
#         with open(file_name, 'a+', encoding='utf-8') as f:
#             f.seek(0)
#             data = f.read()
#             if len(data) > 0:
#                 f.write('\n')

#             last_name = input('Введите фамилию абонента: ')
#             first_name = input('Введите имя абонента: ')
#             patronymic = input('Введите отчество абонента: ')
#             phone = input('Введите номер телефона абонента, если их несколько через запятую: ')#.split(',')
#             email = input('Введите e-mail (пропустить шаг - Enter): ')
#             if "@" in email:
#                 temp = (f'{last_name} {first_name} {patronymic}, тел.: {phone}, e-mail: {email}').rstrip()
#             else:
#                 temp = (f'{last_name} {first_name} {patronymic},  тел.: {phone}').rstrip()            

#             f.write(temp)

#             f.close()
#             print()
#             print("Абонент успешно добавлен")
#             print()
#     except:
#         print("Ошибка")
                    

#     # contact = []
#     # contact.append(int(input('Введите порядковый номер абонента: ')))
#     # contact.append(input('Введите фамилию абонента: '))
#     # contact.append(input('Введите имя абонента: '))
#     # contact.append(input('Введите отчество абонента: '))
#     # contact.append(input('Введите номера телефонов абонента, если их несколько через запятую: ').split(','))
#     # contact.append(input('Введите e-mail (пропустить шаг - Enter): '))
#     # return contact
#     # if "@" in email:
#     #     phone_book[last_name] = {'Фамилия':last_name, 'Имя':first_name, 'Отчество':patronymic, 'тел':phone, 'email': email}
#     #     with open(file_name, 'a', encoding='utf-8') as fd:
#     #         fd.write(phone_book[last_name])
#     # else:
#     #     phone_book[last_name] = {'Фамилия':last_name, 'Имя':first_name, 'Отчество':patronymic, 'тел':phone}
#     #     with open(file_name, 'a', encoding='utf-8') as fd:
#     #         fd.write(phone_book[last_name])
# # Колесов, Радар, Петрович, ['87213562314', ' 89435321365'], radar@mail.ru
# # Прыгучий, Симулятор, Андреевия, ['89765253464']    


# #========================================================Функция для изменения данных

# # ХОЧУ ДОБАВИТЬ - ЕСЛИ СЛОВО ВВЕДЕНО С ОШИБКОЙ

# # def read_file():
# #     file_name = 'phone_book/phonebook.txt'
# #     with open(file_name, 'r', encoding='utf-8') as f:
# #         content = f.read()
# #     return content
# # def write_file(content):
# #     file_name = 'phone_book/phonebook.txt'
# #     with open(file_name, 'w', encoding='utf-8') as f:
# #         new_content = input('Введите на что заменить: ')
# #     f.write(new_content)

# # content = read_file()


# def modify(file_name):
#     file_name = 'phone_book/phonebook.txt'
#     change_contact = input('Выберите:\n1 - для исправления данных определенного контакта по порядковому номеру\n2 - для замены по всему справочнику\n3 - добавить данные\nx - для выхода: ')
#     print()
#     flag_exit = False
#     if change_contact == '1':
#             with open(file_name, 'r', encoding='utf-8') as main:
#                 with open('phone_book/backup_file.txt', 'w', encoding='utf-8') as copy:
#                     for i, line in enumerate(main, 1):
#                         copy.write('{}: {}'.format(i, line))
#                         print(f'{i}.', line.rstrip())
#                     print()
#                     copy.close()
#                     main.close()
#                     number_contact = int(input('Введите № контакта, подлежащего изменениям: '))
#                     print()
#                     try:
#                         with open(file_name, 'r', encoding='utf-8') as source:
#                             content = source.read()
#                             lines = content.splitlines()
#                             lines = lines[number_contact - 1]
#                             source.close()
#                         print(f'Выбранный для внесения изменений контакт:\n{lines}')
#                         print()
#                         was = input('Какое слово желаете изменить? Введите, пожалуйста: ')
#                         is_new = input('Введите на что нужно заменить: ')
#                         with open(file_name, 'r', encoding='utf-8') as f:
#                             data = f.readlines()
#                             with open(file_name, 'w', encoding='utf-8') as copy_one_contact:
#                                 for line in data:
#                                     copy_one_contact.write(line.replace(was, is_new))
                               
#                                 copy_one_contact.close()
#                                 f.close()
#                                 print()
#                                 print("Контакт успешно отредактирован")
#                                 print()
#                     except:
#                         print("Ошибка")
#     elif change_contact == '2':
#         try:
#             with open(file_name, 'r', encoding='utf-8') as source:
#                 content = source.read()
#                 lines = content.splitlines()
#                 source.close()

#             was = input('Какое слово желаете изменить? Введите, пожалуйста: ')
#             is_new = input('Введите на что нужно заменить: ')
#             with open(file_name, 'r', encoding='utf-8') as f:
#                 data = f.readlines()
#                 with open(file_name, 'w', encoding='utf-8') as copy_one_contact:
#                     for line in data:
#                         copy_one_contact.write(line.replace(was, is_new))
#                     copy_one_contact.close()
#                     f.close()
#                     print()
#                     print("Справочник успешно отредактирован")
#                     print()
#         except:
#             print("Ошибка")
#     if change_contact == '3':
#             with open(file_name, 'r', encoding='utf-8') as main:
#                 with open('phone_book/backup_file.txt', 'w', encoding='utf-8') as copy:
#                     for i, line in enumerate(main, 1):
#                         copy.write('{}: {}'.format(i, line))
#                         print(f'{i}.', line.rstrip())
#                     print()
#                     copy.close()
#                     main.close()
#                     number_contact = int(input('Введите № контакта, подлежащего изменениям: '))
#                     print()
#                     try:
#                         with open(file_name, 'r', encoding='utf-8') as source:
#                             content = source.read()
#                             lines = content.splitlines()
#                             lines = lines[number_contact - 1]
#                             source.close()
#                         print(f'Выбранный для внесения изменений контакт:\n{lines}')
#                         print()
#                         answer_add = input('Какой параметр добавим:\n1 - телефон\n2 - e-mail\n3 - прочее\nВвод: ')
#                         # if answer_add == '1':
#                         #     phone = input('Введите номер телефона абонента, если их несколько через запятую: ')#.split(',')
#                         #     with open(file_name, 'r', encoding='utf-8') as f:
#                         #         data = f.readlines()
#                         #         # f.write(data)
#                         #         with open(file_name, 'r', encoding='utf-8') as contact_phone_add:
#                         #             contact_phone_add.write('{}'.format(line))
#                         #             lines = lines[0].split
#                         #             text = lines[0]
#                         #             print(''.join(text[text.find('тел.:') + 6:] + ', ' + phone))


                                
#                         #             contact_phone_add.close()
#                         #             f.close()
#                         #             print()
#                         #             print("Контакт успешно отредактирован")
#                         #             print()
#                         if answer_add == '3':
#                             dop = input('Введите данные для добавления: ')
#                             with open(file_name, 'r', encoding='utf-8') as f:
#                                 data = f.readlines()
#                                 # f.write(data)
#                                 with open(file_name, 'w', encoding='utf-8') as change_one_contact:
#                                     # change_one_contact.write('{}'.format(line))
#                                     for line in data:
#                                         change_one_contact.write(line.replace(lines, lines + ', ' + dop))
#                                     print(line.rstrip())
                                
#                                     change_one_contact.close()
#                                     f.close()
#                                     print()
#                                     print("Контакт успешно отредактирован")
#                                     print()
#                     except:
#                         print("Ошибка")
    
#     elif change_contact == 'x':
#         flag_exit = True

      
# #========================================================Функция для поиска в базе

# def find_by_name(file_name):
#     word_check = input('Пожалуйста, введите ключевое слово для поиска: ')
#     print()
#     with open(file_name, 'r', encoding='utf-8') as f:
#         data = f.readlines()
#         count = 0
#         for line in data:
#             if word_check in line:
#                 count += 1
#         if count > 0:
#             print(f'Вот, что удалось найти в записях по введенному параметру: ' + word_check)
#         else:
#             print(word_check + ' Отсутствует в справочнике')
#         for line in data:
#             if word_check in line.split():
#                 print(line.rstrip())
#         print() 
#     f.close()
#     return('Восполюзуйтесь меню\n')
                            
    


#         # if word_check in data:
#         #     print('Вот, что удалось найти в записях по введенному параметру: ' + word_check)    
#         # else:
#         #     print(word_check + ' Отсутствует в справочнике')
#         # for line in data:
#         #     if word_check in line.split():
#         #         print(line.rstrip())   

    
# #========================================================Функция основная
# def main():
#     file_name = 'phone_book/phonebook.txt'
#     flag_exit = False
#     print('Добро пожаловать в ваш телефонный справочник!')
#     print()
#     while not flag_exit:
#         print('Доступные команды:')
#         print('1 - показать всеx')
#         print('2 - добавить контакт')
#         print('3 - удалить контакт')
#         print('4 - изменить контакт')
#         print('5 - поиск контакта')
#         print()
#         answer = input('Введите № команды или \'x\' для выхода: ')
#         if answer == '1':
            
#             print()
#             show_all(file_name)
#         elif answer == '2':
#             add_new(file_name)
#         elif answer == '3':
#             remove(file_name)
#         elif answer == '4':
#             modify(file_name=file_name)
#         elif answer == '5':
#             print(find_by_name(file_name))
#         elif answer == 'x':
#             print('Хороших контактов вам, да побольше!')
#             flag_exit = True


# if __name__ == '__main__':
#     main()


