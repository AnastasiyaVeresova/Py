# #Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения. 
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
#     for i in res:
#         print(*[f"{x}" for x in i])

# print_operation_table(lambda x, y: x * y)

#-----------------------------------------для автотеста
# import math
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows >= 1 and num_columns >= 1:
#         res = [[operation(i, j) for i in range(1, num_columns + 1)] for j in range(1, num_rows + 1)]
#         for i in res:
#             print(*[f"{x}" for x in i])
            
#     else:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')

# print(print_operation_table(lambda x, y: x - y, 4, 4))
             
# _______________________________________Jот Марата


def print_operation_table1(operation, num_rows, num_columns):
    if num_columns < 2 or num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=' ')
            # вариант с end=' ' не подходит т.к. мы получаем строку:
            # с пробелом в конце '1 2 3 ',
            # а тест ожидает '1 2 3'
        print()


def print_operation_table2(operation, num_rows, num_columns):
    # эта функция проходит проверку на тесте!
    if num_columns < 2 or num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            row = []
            if i == 1:
                # если первая строка, то: 1 2 3 4 ...
                row = list(range(1, num_columns + 1))
            else:
                for j in range(2, num_columns + 1):
                    # можно было бы начать range с 1, тогда было бы:
                    # if j == 1:
                    # ...
                    # и else:
                    # ...
                    if j == 2:
                        #
                        row.append(i)
                    row.append(operation(i, j))
            print(*row)


def print_operation_table3(operation, num_rows, num_columns):
    # можно и с list comprehension:
    if num_columns < 2 or num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            if i == 1:
                row = list(range(1, num_columns + 1))
            else:
                row = [i if j == 1 else operation(i, j) for j in range(1, num_columns + 1)]
            print(*row)


print('  [!] x * y')
print_operation_table2(lambda x, y: x * y, 3, 3)
print()
print_operation_table3(lambda x, y: x * y, 3, 3)

print('\n  [!] x + y')
print_operation_table2(lambda x, y: x + y, 4, 4)
print()
print_operation_table3(lambda x, y: x + y, 4, 4)

print('\n  [!] x - y')
print_operation_table2(lambda x, y: x - y, 5, 5)
print()
print_operation_table3(lambda x, y: x - y, 5, 5)

print('\n  [!] x / y')
print_operation_table2(lambda x, y: x / y, 4, 4)
print()
print_operation_table3(lambda x, y: x / y, 4, 4)