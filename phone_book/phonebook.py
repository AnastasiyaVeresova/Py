import os

#========================================================Функция для подсчета строк в файле

def count_nonempty_lines(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            return len([line for line in f if line.rstrip()])
    else:
        return 0
##============================================для подсчета
    # with open('phone_book/phonebook.txt', 'r', encoding='utf-8') as source:
    #     count = 0
    #     s = source.readline()
    #     while s != '':
    #         s=source.readline()
    #         count += 1
    # print(count)
    # source.close()
#========================================================Функция для удаления   

def remove(file_name:str):
    file_name = 'phone_book/phonebook.txt'
    flag_exit = False
    while not flag_exit:
        for_remove = input('Выберите:\n1 - для удаления определенного контакта по порядковому номеру\n2 - для полного очищения телефонного справочника\nx - для выхода: ')
        print()
        if for_remove == '1':
            with open(file_name, 'r', encoding='utf-8') as main:
                with open('phone_book/copy_file_name.txt', 'w', encoding='utf-8') as copy:
                    for i, line in enumerate(main, 1):
                        copy.write('{}: {}'.format(i, line))
                        print(f'{i}.', line.rstrip())
                    print()
                    copy.close()
                    main.close()
                    position_delete = int(input('Введите № позиции для удаления: '))
                    try:
                        with open(file_name, 'r', encoding='utf-8') as source:
                            content = source.read()
                            lines = content.splitlines()
                            del lines[position_delete - 1]
                            new_content = '\n'.join(lines)
                        with open(file_name, 'w', encoding='utf-8') as source:
                            source.write(new_content)
                            source.close()
                        print("Контакт удален")
                        print()
                    except:
                        print("Ошибка")
        elif for_remove == '2':
            try:
                open(file_name, 'w').close()
                print("Телефонная книга успешно очищена")
                print()
            except:
                print("Ошибка")
        elif for_remove == 'x':
            flag_exit = True

#========================================================Функция для показа всех записей в справочнике
def show_all(file_name:str):
    if count_nonempty_lines(file_name) == 0:
        print('Телефонная книга пуста > выберите 2 для добавления контакта')
        print()
    else:
        print('Список ваших контактов: ')
        with open(file_name, 'r',encoding='utf-8') as f:
            data = f.readlines()
            op = f.readline()
            i = 0
            for lines in data:
                if len(lines) > 1:
                    i += 1              
                    print(str(i) + '. ' + lines.rstrip()) 

            print()
            # file_name.close()

#========================================================Функция для добавления нового контакта

def add_new(file_name):
    try:
        with open(file_name, 'a+', encoding='utf-8') as f:
            f.seek(0)
            data = f.read()
            if len(data) > 0:
                f.write('\n')

            last_name = input('Введите фамилию абонента: ')
            first_name = input('Введите имя абонента: ')
            patronymic = input('Введите отчество абонента: ')
            phone = input('Введите номера телефонов абонента, если их несколько через запятую: ')#.split(',')
            email = input('Введите e-mail (пропустить шаг - Enter): ')
            if "@" in email:
                temp = (f'{last_name} {first_name} {patronymic}, {phone}, {email}').rstrip()
            else:
                temp = (f'{last_name} {first_name} {patronymic}, {phone}').rstrip()            

            f.write(temp)

            f.close()
            print()
            print("Абонент успешно добавлен")
            print()
    except:
        print("Ошибка")
                    

    # contact = []
    # contact.append(int(input('Введите порядковый номер абонента: ')))
    # contact.append(input('Введите фамилию абонента: '))
    # contact.append(input('Введите имя абонента: '))
    # contact.append(input('Введите отчество абонента: '))
    # contact.append(input('Введите номера телефонов абонента, если их несколько через запятую: ').split(','))
    # contact.append(input('Введите e-mail (пропустить шаг - Enter): '))
    # return contact
    # if "@" in email:
    #     phone_book[last_name] = {'Фамилия':last_name, 'Имя':first_name, 'Отчество':patronymic, 'тел':phone, 'email': email}
    #     with open(file_name, 'a', encoding='utf-8') as fd:
    #         fd.write(phone_book[last_name])
    # else:
    #     phone_book[last_name] = {'Фамилия':last_name, 'Имя':first_name, 'Отчество':patronymic, 'тел':phone}
    #     with open(file_name, 'a', encoding='utf-8') as fd:
    #         fd.write(phone_book[last_name])
# Колесов, Радар, Петрович, ['87213562314', ' 89435321365'], radar@mail.ru
# Прыгучий, Симулятор, Андреевия, ['89765253464']    


#========================================================Функция для изменения данных

# ХОЧУ ДОБАВИТЬ - ЕСЛИ СЛОВО ВВЕДЕНО С ОШИБКОЙ

# def read_file():
#     file_name = 'phone_book/phonebook.txt'
#     with open(file_name, 'r', encoding='utf-8') as f:
#         content = f.read()
#     return content
# def write_file(content):
#     file_name = 'phone_book/phonebook.txt'
#     with open(file_name, 'w', encoding='utf-8') as f:
#         new_content = input('Введите на что заменить: ')
#     f.write(new_content)

# content = read_file()


def modify(file_name:str):
    file_name = 'phone_book/phonebook.txt'
    change_contact = input('Выберите:\n1 - для исправления данных определенного контакта по порядковому номеру\n2 - для замены всех вхождений слова\nx - для выхода: ')
    print()
    if change_contact == '1':
            with open(file_name, 'r', encoding='utf-8') as main:
                with open('phone_book/copy_file_name.txt', 'w', encoding='utf-8') as copy:
                    for i, line in enumerate(main, 1):
                        copy.write('{}: {}'.format(i, line))
                        print(f'{i}.', line.rstrip())
                    print()
                    copy.close()
                    main.close()
                    number_contact = int(input('Введите № контакта, подлежащего изменениям: '))
                    print()
                    try:
                        with open(file_name, 'r', encoding='utf-8') as source:
                            content = source.read()
                            lines = content.splitlines()
                            lines = lines[number_contact - 1]
                            source.close()
                        print(f'Выбранный для внесения изменений контакт:\n{lines}')
                        print()
                        was = input('Какое слово желаете изменить? Введите, пожалуйста: ')
                        is_new = input('Введите на что нужно заменить: ')
                        with open(file_name, 'r', encoding='utf-8') as f:
                            data = f.readlines()
                            with open(file_name, 'w', encoding='utf-8') as copy_one_contact:
                                for line in data:
                                    copy_one_contact.write(line.replace(was, is_new))
                                copy_one_contact.close()
                                f.close()
                                print()
                                print("Контакт успешно отредактирован")
                                print()
                    except:
                        print("Ошибка")
    elif change_contact == '2':
        try:
            with open(file_name, 'r', encoding='utf-8') as source:
                content = source.read()
                lines = content.splitlines()
                source.close()

            was = input('Какое слово желаете изменить? Введите, пожалуйста: ')
            is_new = input('Введите на что нужно заменить: ')
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.readlines()
                with open(file_name, 'w', encoding='utf-8') as copy_one_contact:
                    for line in data:
                        copy_one_contact.write(line.replace(was, is_new))
                    copy_one_contact.close()
                    f.close()
                    print()
                    print("Справочник успешно отредактирован")
                    print()
        except:
            print("Ошибка")
    elif change_contact == 'x':
        flag_exit = True

      
#========================================================Функция для поиска в базе

def find_by_name(file_name):
    word_check = input('Пожалуйста, введите ключевое слово для поиска: ')
    print()
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        # if word_check in data:
        #     print('Вот, что удалось найти в записях по введенному параметру: ' + word_check)    
        # else:
        #     print(word_check + ' Отсутствует в справочнике')
        for line in data:
            if word_check in line.split():
                print(line.rstrip())

#========================================================Функция основная
def main():
    file_name = 'phone_book/phonebook.txt'
    flag_exit = False
    print('Добро пожаловать в ваш телефонный справочник!')
    print()
    while not flag_exit:
        print('Доступные команды:')
        print('1 - показать всеx')
        print('2 - добавить контакт')
        print('3 - удалить контакт')
        print('4 - изменить контакт')
        print('5 - поиск контакта')
        print()
        answer = input('Введите № команды или \'x\' для выхода: ')
        if answer == '1':
            
            print()
            show_all(file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name=file_name)
        elif answer == '5':
            print(find_by_name(file_name))
        elif answer == 'x':
            print('Хороших контактов вам, да побольше!')
            flag_exit = True


if __name__ == '__main__':
    main()

