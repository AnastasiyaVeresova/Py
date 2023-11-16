
Не все тесты пройдены, есть ошибки :(


Количество затраченных попыток: 4

Время выполнения: 1.342786 сек

Общая статистика
Всего тестов: 6. Пройдено: 2. Не пройдено: 4.

Подробную информацию по каждому тесту смотрите ниже.

Тест 1
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def print_operation_table(operation, num_rows, num_columns):
    if num_rows >= 1 and num_columns >= 1:
        res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
        for i in res:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
        
# print_operation_table(lambda x, y: x * y, 3, 3)

              

print_operation_table(lambda x, y: x * y, 3, 3)
Тест 2
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def print_operation_table(operation, num_rows, num_columns):
    if num_rows >= 1 and num_columns >= 1:
        res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
        for i in res:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
        
# print_operation_table(lambda x, y: x * y, 3, 3)

              

print_operation_table(lambda x, y: x + y, 4, 4)


Ожидаемый ответ:

1 2 3 4
2 4 5 6
3 5 6 7
4 6 7 8

Ваш ответ:

2 3 4 5
3 4 5 6
4 5 6 7
5 6 7 8
Тест 3
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def print_operation_table(operation, num_rows, num_columns):
    if num_rows >= 1 and num_columns >= 1:
        res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
        for i in res:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
        
# print_operation_table(lambda x, y: x * y, 3, 3)

              

print_operation_table(lambda x, y: x - y, 5, 5)


Ожидаемый ответ:

1 2 3 4 5
2 0 -1 -2 -3
3 1 0 -1 -2
4 2 1 0 -1
5 3 2 1 0

Ваш ответ:

0 1 2 3 4
-1 0 1 2 3
-2 -1 0 1 2
-3 -2 -1 0 1
-4 -3 -2 -1 0
Тест 4
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def print_operation_table(operation, num_rows, num_columns):
    if num_rows >= 1 and num_columns >= 1:
        res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
        for i in res:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
        
# print_operation_table(lambda x, y: x * y, 3, 3)

              

print_operation_table(lambda x, y: x * y, 1, 2)


Ожидаемый ответ:

ОШИБКА! Размерности таблицы должны быть больше 2!

Ваш ответ:

1 2
Тест 5
Тест не пройден ✗

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def print_operation_table(operation, num_rows, num_columns):
    if num_rows >= 1 and num_columns >= 1:
        res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
        for i in res:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
        
# print_operation_table(lambda x, y: x * y, 3, 3)

              

print_operation_table(lambda x, y: x / y, 4, 4)


Ожидаемый ответ:

1 2 3 4
2 1.0 0.6666666666666666 0.5
3 1.5 1.0 0.75
4 2.0 1.3333333333333333 1.0

Ваш ответ:

1.0 2.0 3.0 4.0
0.5 1.0 1.5 2.0
0.3333333333333333 0.6666666666666666 1.0 1.3333333333333333
0.25 0.5 0.75 1.0
Тест 6
Тест пройден успешно ✓

Формулировка:

* Итоговый код для проверки. Иногда добавляем что-то от себя :)


import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже






#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def print_operation_table(operation, num_rows, num_columns):
    if num_rows >= 1 and num_columns >= 1:
        res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
        for i in res:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
        
# print_operation_table(lambda x, y: x * y, 3, 3)

              

print_operation_table(lambda x, y: x * y)
