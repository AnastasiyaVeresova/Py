# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 1. Программа должна выводить данные 2. Программа должна сохранять данные в текстовом файле 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 4. Использование функций. Ваша программа не должна быть линейной

# import sqlite3 as sl

# conn = sl.connect("test.db")

# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS users
#                (ID integer primary key,
#                name text)
#                ;""")
# cursor.execute("INSERT INTO users Values (1, 'Ваня', 'Иванов');")
# cursor.execute("SELECT * FROM users;")
# print(cursor.fetchall())

#--------------------------------------------------------------- 

# def new():

#     name = input("Введите имя абонента ")

#     phone = list(input("Введите телефон абонента через запятую ")).split(',')

#     email = input("Введите электронный адрес ")

#     if "@" in email:

#         phone_book[name] = {'phones': phone, 'email': email}

#     else:

#         phone_book[name] = {'phones': phone}

       

# def save():

#     with open(phone_book, "w", encoding = "utf-8")

 

       

    

# phone_book = {"дядя Ваня": {'phones': [1321231, 121213],

#                             'email': "123@mail.ru"},

#             "дядя Вася": {'phones': [55555]}

# }

 

# while True:

#     command = input("Введите команду ")

#     if command == "/start":

#         print("Добро пожаловать в вашу телефонную книгу")

#     if command == "/stop":

#         break

#     elif command == "/all":

#         print(phone_book.keys())

#     elif command == "/new":

#         new()

#     elif command == "/show":

#         name_1 = input("Введите имя абонента ")

#         print(phone_book[name_1])

#---------------------------------------------------------------------------------------------------
def show_all(file_name:str):
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))


def remove(file_name:str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        data.remove(s)
    with open(file_name, 'w',encoding='utf-8') as f:
        f.writelines(data)
        
        

def modify(file_name:str):
    # print("Введите данные для поиска:\n")
    # last_name = input('Введите фамилию: ')
    # first_name = input('Введите имя: ')
    # patronymic = input('Введите отчество: ')
    # phone_number = input('Введите номер телефона: ')
    
    old_data = find_by_attribute(file_name, True)
    
    print("Введите новые данные:\n")
    last_name_ = input('Введите фамилию: ')
    first_name_ = input('Введите имя: ')
    patronymic_ = input('Введите отчество: ')
    phone_number_ = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f'{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n'
        
    with open(file_name, 'w',encoding='utf-8') as f:\
        f.writelines(data)
        
        
def find_by_attribute(file_name:str,option: bool):
    
    c = input("Введите 1 для поиска по фамилии, 2 для поиска по имени")
    
        
    opt = 0
    if c == '1':
        opt = 0
    elif c == '2':
        opt = 1
        
    attr = input("Введите имя/фамилию для поиска")
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == attr,data))
        print(list(zip(range(1,len(data)+1),data)))
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
            id = input("Введите id нужного пользователя: ")
        return data[int(id)-1]


def add_new(file_name: str):
    # data = input('Введите ФИО и номер телефона через пробел: ')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    # Иванов Петр Сидорович 1234567
    # Петров Иван Сидорович 76543231
    # Сидоров, Петр, Степанович, 7777777
    # 'cp-1251'
    # f = open(file_name, 'a', encoding='utf-8')
    # f.close()
    # print('dssdfsdsdfsd\n\n\nssdf\'sdf\'sdf')
    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')

 
def main():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить все запись')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - поиск записи по имени/фамилии')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name=file_name)
        elif answer == '5':
            print(find_by_attribute(file_name,False))
        elif answer == 'x':
            flag_exit = True

if __name__ == '__main__':
    main()
    
    # print('123')
    # print(__name__)
# else:
#     print('123')
#     print('отрабатывает else')
#     print(__name__)

#------------------------------------------------------------------------------------------

import codecs
import os

clear = lambda: os.system('cls')

# ввод записи
def putNewLine():
    record = []
    record.append(input('Введите фамилию: ').upper())
    record.append(input('Введите имя: ').upper())
    record.append(input('Введите отчество: ').upper())
    record.append(input('Введите номер телефона: ').upper())
    return record

# считаем список строк, чтобы присвоить номер записи
def count_nonempty_lines(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return len([line for line in f if line.strip()])
    else:
        return 0

# добавление записи в файл
def inputDataFile(filename,dataInput):
    dataInput.insert(0,str(count_nonempty_lines(filename) + 1))
    output_string = '\t'.join(dataInput)
    data = open(fileName, 'a')
    data.writelines(f'{output_string}\t' + '\n')
    data.close()

# вывести файл на печать
def outputDataFile(filename):
    print('╒════════════════╤════════════════╤════════════════╤════════════════╤════════════════╕')
    print('│ № записи       │ Фамилия        │ Имя            │ Отчество       │ Телефон        │')
    with open(filename, 'r') as fp:
        data = [line.split('\t') for line in fp]
    for i in data:
        i.remove('\n')
        print('├────────────────┼────────────────┼────────────────┼────────────────┼────────────────┤')
        print('│', end='')
        for value in i:
            print("{0:>16}".format(value), end='│')
        print()
    print('╘════════════════╧════════════════╧════════════════╧════════════════╧════════════════╛')

# поиск записи в справочнике
def findRecord(filename,record):
    temp = 0
    print()
    with open(filename, 'r') as fp:
        data = [line.split('\t') for line in fp]
    for i in data:
        i.remove('\n')
        if record.upper() in i:
            print(*i)
            temp += 1
    if temp == 0:
        print('Такой записи нет в справочнике')

def main(filename):
    while True:
        clear()
        print('Инструкция по работе с программой:')
        print('Введите: 1 - просмотр справочника. Введите: 2 - добавить запись. Введите: 3 - найти пользователя')
        print('Введите любое другое число для выхода из программы ')
        func_num = int(input('Сделайте Ваш выбор: '))
        if func_num == 1:
            if count_nonempty_lines(filename) == 0:
                print('Справочник пуст или не существует. Введите хотя бы одну запись для начала работы')
            else:
                outputDataFile(fileName)
            print()
        elif func_num == 2:
            newRecord = putNewLine()
            inputDataFile(filename, newRecord)
        elif func_num == 3:
            if count_nonempty_lines(filename) == 0:
                print('Справочник пуст или не существует. Введите хотя бы одну запись для начала работы')
            else:
                searchingRecord = input('Введите запись для поиска: ')
                findRecord(filename, searchingRecord)
            print()
        else: break

fileName = 'telephonebook1.txt'
main(fileName)
