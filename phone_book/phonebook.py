import os
import re


# ========================================================Функция для подсчета строк в файле

def count_nonempty_lines(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            return len([line for line in f if line.rstrip()])
    else:
        return 0


def remove(file_name: str):
    file_name = 'phone_book/phonebook.txt'
    flag_exit = False
    while not flag_exit:
        for_remove = input(
            'Выберите:\n1 - для удаления определенного контакта по порядковому номеру\n2 - для полного очищения телефонного справочника\nx - для выхода: ')
        print()
        if for_remove == '1':
            with open(file_name, 'r', encoding='utf-8') as main:
                with open('phone_book/backup_file.txt', 'w',
                          encoding='utf-8') as copy:
                    for i, line in enumerate(main, 1):
                        copy.write('{}: {}'.format(i, line))
                        print(f'{i}.', line.rstrip())
                    print()
                    position_delete = int(
                        input('Введите № позиции для удаления: '))
                    try:
                        with open(file_name, 'r', encoding='utf-8') as source:
                            content = source.read()
                            lines = content.splitlines()
                            del lines[position_delete - 1]
                            new_content = '\n'.join(lines)
                        with open(file_name, 'w', encoding='utf-8') as source:
                            source.write(new_content)
                        print("Контакт удален")
                        print()
                    except Exception as err:
                        print("Ошибка:", err)
        elif for_remove == '2':
            try:
                open(file_name, 'w').close()
                print("Телефонная книга успешно очищена")
                print()
            except Exception as err:
                print("Ошибка:", err)
        elif for_remove == 'x':
            flag_exit = True


# ========================================================Функция для показа всех записей в справочнике
def show_all(file_name: str):
    if count_nonempty_lines(file_name) == 0:
        print('Телефонная книга пуста > выберите 2 для добавления контакта')
        print()
    else:
        print('Список ваших контактов: ')
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.readlines()
            i = 0
            for lines in data:
                if len(lines) > 1:
                    i += 1
                    print(str(i) + '. ' + lines.rstrip())
            print()

# ========================================================Функция для добавления нового контакта

def add_new(file_name):
    try:
        with open(file_name, 'a', encoding='utf-8') as f:

            last_name = input('Введите фамилию абонента: ')
            first_name = input('Введите имя абонента: ')
            patronymic = input('Введите отчество абонента: ')
            phone = input(
                'Введите номер телефона абонента, если их несколько через запятую: ')  # .split(',')
            email = input('Введите e-mail (пропустить шаг - Enter): ')
            if "@" in email:
                temp = (
                    f'{last_name} {first_name} {patronymic}, тел.: {phone}, e-mail: {email}\n')
            else:
                temp = (
                    f'{last_name} {first_name} {patronymic},  тел.: {phone}\n')

            f.write(temp)

            print()
            print("Абонент успешно добавлен")
            print()
    except Exception as err:
        print("Ошибка:", err)

# ========================================================Функция для изменения данных


def modify(file_name):
    file_name = 'phone_book/phonebook.txt'
    change_contact = input(
        'Выберите:\n1 - для исправления данных определенного контакта по порядковому номеру\n2 - для замены по всему справочнику\n3 - добавить данные\nx - для выхода: ')
    print()
    flag_exit = False
    if change_contact == '1':
        with open(file_name, 'r', encoding='utf-8') as main:
            with open('phone_book/backup_file.txt', 'w',
                      encoding='utf-8') as copy:
                for i, line in enumerate(main, 1):
                    copy.write('{}: {}'.format(i, line))
                    print(f'{i}.', line.rstrip())
                print()
                number_contact = int(
                    input('Введите № контакта, подлежащего изменениям: '))
                print()
                try:
                    with open(file_name, 'r', encoding='utf-8') as source:
                        content = source.read()
                        lines = content.splitlines()
                        lines = lines[number_contact - 1]
                        source.close()
                    print(
                        f'Выбранный для внесения изменений контакт:\n{lines}')
                    print()
                    was = input(
                        'Какое слово желаете изменить? Введите, пожалуйста: ')
                    is_new = input('Введите на что нужно заменить: ')
                    with open(file_name, 'r', encoding='utf-8') as f:
                        data = f.readlines()
                        with open(file_name, 'w',
                                  encoding='utf-8') as copy_one_contact:
                            for line in data:
                                copy_one_contact.write(
                                    line.replace(was, is_new))

                            copy_one_contact.close()
                            print()
                            print("Контакт успешно отредактирован")
                            print()
                except Exception as err:
                    print("Ошибка:", err)
    elif change_contact == '2':
        try:
            with open(file_name, 'r', encoding='utf-8') as source:
                content = source.read()
                lines = content.splitlines()

            was = input('Какое слово желаете изменить? Введите, пожалуйста: ')
            is_new = input('Введите на что нужно заменить: ')
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.readlines()
                with open(file_name, 'w',
                          encoding='utf-8') as copy_one_contact:
                    for line in data:
                        copy_one_contact.write(line.replace(was, is_new))
                    copy_one_contact.close()
                    print()
                    print("Справочник успешно отредактирован")
                    print()
        except Exception as err:
            print("Ошибка:", err)
    if change_contact == '3':
        with open(file_name, 'r', encoding='utf-8') as main:
            with open('phone_book/backup_file.txt', 'w',
                      encoding='utf-8') as copy:
                for i, line in enumerate(main, 1):
                    copy.write('{}: {}'.format(i, line))
                    print(f'{i}.', line.rstrip())
                print()
                number_contact = int(
                    input('Введите № контакта, подлежащего изменениям: '))
                print()
                try:
                    with open(file_name, 'r', encoding='utf-8') as source:
                        content = source.read()
                        lines = content.splitlines()
                        lines = lines[number_contact - 1]
                    print(
                        f'Выбранный контакт:\n{lines}')
                    print()

                    dop = input('Введите данные для добавления: ')
                    with open(file_name, 'r', encoding='utf-8') as f:
                        data = f.readlines()
                        with open(file_name, 'w', encoding='utf-8') as change_one_contact:
                            for line in data:
                                change_one_contact.write(line.replace(lines, lines + ', ' + dop))
                            print(line.rstrip())
                            print()
                            print("Контакт успешно отредактирован")
                            print()
                except Exception as err:
                    print("Ошибка:", err)

    elif change_contact == 'x':
        flag_exit = True

# ========================================================Функция для поиска в базе

def find_by_name(file_name):
    word_check = input('Пожалуйста, введите ключевое слово для поиска: ')
    print()
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        found_contacts = []
        for line in data:
            if word_check in line:
                found_contacts.append(line)
        if found_contacts:
            print(
                f'Вот, что удалось найти в записях по введенному параметру: ' + word_check)
            for line in data:
                if word_check in line.split():
                    print(line.rstrip())
        else:
            print(word_check + ' Отсутствует в справочнике')
        print()

    return 'Воспользуйтесь меню\n'

# ========================================================Функция основная
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
